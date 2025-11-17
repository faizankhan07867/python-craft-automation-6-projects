# 01-bulk-rename.py

import os

folder = "images"  # Apne images folder ka naam daal do
os.makedirs(folder, exist_ok=True)

print("Bulk File Renamer - Craft Products")
pattern = input("Enter naming pattern (e.g., vase_, candle_, macrame_): ")
start_num = int(input("Starting number: "))

files = [f for f in os.listdir(folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
files.sort()

for i, file in enumerate(files):
    ext = file.split('.')[-1]
    old_path = os.path.join(folder, file)
    new_name = f"{pattern}{start_num + i}.{ext}"
    new_path = os.path.join(folder, new_name)
    os.rename(old_path, new_path)
    print(f"Renamed: {file} → {new_name}")

print("All files renamed successfully!")
