import os
import random
import shutil

# --- Configuration ---
SOURCE_IMAGES = "auto_dataset/images"
SOURCE_LABELS = "auto_dataset/labels"
DATASET_DIR = "dataset"

def split_and_prep_dataset():
    # 1. Create the strict YOLO folder structure
    for split in ["train", "valid"]:
        os.makedirs(os.path.join(DATASET_DIR, split, "images"), exist_ok=True)
        os.makedirs(os.path.join(DATASET_DIR, split, "labels"), exist_ok=True)

    # 2. Match images with their label files
    images = [f for f in os.listdir(SOURCE_IMAGES) if f.endswith(".jpg")]
    matched_data = []
    
    for img in images:
        label = img.replace(".jpg", ".txt")
        if os.path.exists(os.path.join(SOURCE_LABELS, label)):
            matched_data.append((img, label))
            
    print(f"Found {len(matched_data)} fully labeled images.")

    # 3. Shuffle and split (80% Train, 20% Valid)
    random.seed(42) # Keeps the shuffle consistent if you run it again
    random.shuffle(matched_data)
    
    split_index = int(len(matched_data) * 0.8)
    train_data = matched_data[:split_index]
    valid_data = matched_data[split_index:]

    # 4. Copy files to their new destinations
    def copy_files(data_list, split_name):
        for img, label in data_list:
            shutil.copy(os.path.join(SOURCE_IMAGES, img), 
                        os.path.join(DATASET_DIR, split_name, "images", img))
            shutil.copy(os.path.join(SOURCE_LABELS, label), 
                        os.path.join(DATASET_DIR, split_name, "labels", label))

    print("Copying files to train and valid folders...")
    copy_files(train_data, "train")
    copy_files(valid_data, "valid")

    # 5. Generate the data.yaml file automatically
    yaml_content = f"""path: {os.path.abspath(DATASET_DIR)}
train: train/images
val: valid/images

nc: 1
names: ['Article']
"""
    yaml_path = os.path.join(DATASET_DIR, "data.yaml")
    with open(yaml_path, "w") as f:
        f.write(yaml_content)

    print(f"\nSuccess! Dataset is ready for training.")
    print(f"Train set: {len(train_data)} images")
    print(f"Valid set: {len(valid_data)} images")
    print(f"Configuration file saved to: {yaml_path}")

if __name__ == "__main__":
    split_and_prep_dataset()