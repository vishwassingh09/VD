import os
import requests
from PIL import Image
from io import BytesIO

# --- CONFIGURATION ---
API_URL = "https://enewspapr.com/epaper-api/epaper-api.php?issueID=DAINIKPRA_PUNE_20260805&operation=getAllArticleByArticleId&cache=random"

# Keep the same output folders
OUTPUT_DIR = "auto_dataset"
IMAGES_DIR = os.path.join(OUTPUT_DIR, "images")
LABELS_DIR = os.path.join(OUTPUT_DIR, "labels")

os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(LABELS_DIR, exist_ok=True)

def generate_bulk_yolo_data():
    print("Fetching layout data for the entire issue...")
    
    # 1. Hit the API
    response = requests.get(API_URL)
    if response.status_code != 200:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return
        
    data_list = response.json()
    
    # Ensure it's a list so we can loop through it safely
    if not isinstance(data_list, list):
        data_list = [data_list]

    print(f"Found {len(data_list)} pages in this issue. Starting mass download...\n")

    # 2. Loop through EVERY page in the newspaper
    for page_data in data_list:
        image_name = page_data.get("imagename")
        if not image_name:
            continue
            
        print(f"Processing {image_name}...")
        
        # Download the Image
        image_url = page_data.get("fullImagePath") 
        if not image_url:
            print("  -> No image URL found, skipping...")
            continue
            
        try:
            img_response = requests.get(image_url)
            img = Image.open(BytesIO(img_response.content))
            
            image_path = os.path.join(IMAGES_DIR, image_name)
            img.convert('RGB').save(image_path, "JPEG")
            img_width, img_height = img.size
        except Exception as e:
            print(f"  -> Failed to download image: {e}")
            continue

        # Process the Articles and YOLO Math
        articles = page_data.get("Articles", [])
        txt_filename = os.path.splitext(image_name)[0] + ".txt"
        txt_filepath = os.path.join(LABELS_DIR, txt_filename)
        
        valid_boxes = 0
        with open(txt_filepath, "w") as f:
            for item in articles:
                article = item.get("Article", {})
                
                try:
                    x1 = float(article.get("x1", 0))
                    y1 = float(article.get("y1", 0))
                    x2 = float(article.get("x2", 0))
                    y2 = float(article.get("y2", 0))
                    
                    box_width = x2 - x1
                    box_height = y2 - y1
                    
                    # Skip broken coordinates where width or height is 0 or negative
                    if box_width <= 0 or box_height <= 0:
                        continue 
                        
                    center_x = x1 + (box_width / 2.0)
                    center_y = y1 + (box_height / 2.0)
                    
                    norm_center_x = center_x / img_width
                    norm_center_y = center_y / img_height
                    norm_width = box_width / img_width
                    norm_height = box_height / img_height
                    
                    class_id = 0
                    yolo_line = f"{class_id} {norm_center_x:.6f} {norm_center_y:.6f} {norm_width:.6f} {norm_height:.6f}\n"
                    f.write(yolo_line)
                    valid_boxes += 1
                except ValueError:
                    continue # Skip if data is missing or corrupted
        
        print(f"  -> Saved {valid_boxes} bounding boxes.")

    print("\nBulk download complete! Check the 'auto_dataset' folder.")

if __name__ == "__main__":
    generate_bulk_yolo_data()