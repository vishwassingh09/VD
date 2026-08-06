from ultralytics import YOLO

def test_model():
    # 1. Load YOUR custom-trained weights from the folder in your screenshot
    model = YOLO("runs/detect/layout_analysis/run_1-2/weights/best.pt")

    # 2. Pick a test image (replace with the exact name of a new JPG you want to test)
    # E.g., put a new image in your Machine_Learning folder and name it 'test_page.jpg'
    test_image_path = "test_page.jpg" 

    # 3. Run inference
    print(f"Testing model on {test_image_path}...")
    results = model.predict(
        source=test_image_path,
        conf=0.50, # Only show boxes the model is at least x% confident about
        save=True  # Saves the output image with boxes drawn
    )

    print("\nDone! Check the new 'runs/detect/predict' folder to see the visual results.")

if __name__ == "__main__":
    test_model()