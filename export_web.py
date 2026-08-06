from ultralytics import YOLO
import json

def export_to_web_json():
    # 1. Load your trained model
    model = YOLO("runs/detect/layout_analysis/run_1-2/weights/best.pt")

    # 2. Pick a test image (this should be page 1 of today's newspaper)
    test_image_path = "test_page.jpg" 

    print(f"Running inference on {test_image_path}...")
    results = model.predict(source=test_image_path, conf=0.25)
    
    web_boxes = []
    
    # 3. Extract and convert coordinates to CSS percentages
    for box in results[0].boxes:
        # Get normalized xywh (center_x, center_y, width, height)
        x_c, y_c, w, h = box.xywhn[0].tolist()
        
        # Convert YOLO center points to CSS Top/Left anchor points
        left_percent = (x_c - (w / 2)) * 100
        top_percent = (y_c - (h / 2)) * 100
        width_percent = w * 100
        height_percent = h * 100
        
        web_boxes.append({
            "left": f"{left_percent:.2f}%",
            "top": f"{top_percent:.2f}%",
            "width": f"{width_percent:.2f}%",
            "height": f"{height_percent:.2f}%",
            "link": "#" # Placeholder for future article links
        })

    # 4. Save to a JSON file that the web frontend can read
    json_filename = "page_1_layout.json"
    with open(json_filename, "w") as f:
        json.dump(web_boxes, f, indent=4)
        
    print(f"Success! Extracted {len(web_boxes)} articles to {json_filename}")

if __name__ == "__main__":
    export_to_web_json()