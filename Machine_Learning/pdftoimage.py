import os
from pdf2image import convert_from_path

# --- Configuration ---
PDF_DIR = "data/raw_pdfs"       # Folder containing your newspaper PDFs
OUTPUT_DIR = "data/images"      # Folder where the JPGs will be saved
DPI = 300                       # 300 is great for OCR/Layout detection. Lower to 200 if files are too big.

# [WINDOWS USERS ONLY]: Paste the path to your Poppler bin folder here. 
# Mac/Linux users can leave this as None.
POPPLER_PATH = r"C:\poppler\Library\bin" 

def convert_pdfs_to_images():
    # Ensure output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Loop through all files in the PDF directory
    for filename in os.listdir(PDF_DIR):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(PDF_DIR, filename)
            print(f"Converting: {filename}...")

            try:
                # Convert the PDF to a list of images (one per page)
                images = convert_from_path(
                    pdf_path, 
                    dpi=DPI, 
                    
                )

                # Save each page as a separate JPG
                for page_num, image in enumerate(images):
                    # Format: filename_page_1.jpg
                    base_name = os.path.splitext(filename)[0]
                    image_filename = f"{base_name}_page_{page_num + 1}.jpg"
                    image_path = os.path.join(OUTPUT_DIR, image_filename)
                    
                    image.save(image_path, "JPEG")
                    print(f"  -> Saved {image_filename}")
            
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    print("\nConversion complete! Your images are ready for YOLO annotation.")

if __name__ == "__main__":
    convert_pdfs_to_images()