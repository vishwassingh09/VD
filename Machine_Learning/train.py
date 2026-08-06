from ultralytics import YOLO
import torch

def train_model():
    # 1. Verify GPU availability before starting
    if torch.cuda.is_available():
        print(f"GPU detected: {torch.cuda.get_device_name(0)}")
    else:
        print("WARNING: GPU not detected. Training on CPU will be extremely slow.")

    # 2. Load a pre-trained YOLO model
    # We are using the 'nano' version ('n') because it is the smallest and fastest.
    # It requires the least amount of VRAM while still being highly accurate for layouts.
    model = YOLO("yolov8n.pt") 

    # 3. Train the model with strict memory constraints
    print("Starting training...")
    
    results = model.train(
        data="dataset/data.yaml",  # Path to your dataset configuration file
        epochs=50,                 # How many times to loop through the dataset
        imgsz=640,                 # Image resolution. Do not exceed 640 on 4GB VRAM.
        batch=4,                   # CRITICAL: Keep this at 2 or 4 to prevent OOM errors.
        device=0,                  # Forces training on your primary GPU (GTX 1650).
        amp=True,                  # CRITICAL: Enables Automatic Mixed Precision (saves massive VRAM).
        workers=2,                 # Limits CPU data-loading threads so RAM doesn't bottleneck.
        project="layout_analysis", # Folder where your trained weights will be saved
        name="run_1"               # Name of this specific training run
    )

    print("\nTraining complete! Check the 'layout_analysis/run_1' folder for your weights.")

if __name__ == "__main__":
    # This block is required in Windows to prevent multiprocessing crash loops
    train_model()