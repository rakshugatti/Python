import os
import shutil

BASE_DIR = "OfficeFiles"

# (a) List all files recursively
def list_files_recursively(directory):
    print(f"\nListing all files in '{directory}' recursively:")
    for root, dirs, files in os.walk(directory):
        for file in files:
            print(os.path.join(root, file))

# (b) Create directory structure
def create_directory_structure():
    paths = [
        os.path.join(BASE_DIR, "HR", "Projects"),
        os.path.join(BASE_DIR, "IT", "Projects"),
        os.path.join(BASE_DIR, "Finance", "Projects"),
    ]
    for path in paths:
        os.makedirs(path, exist_ok=True)
    print("\nDirectory structure created successfully!")

# (c) Rename files matching a pattern (e.g., 'draft' → 'final')
def rename_files_pattern(directory, pattern="draft", replacement="final"):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if pattern in file:
                old_path = os.path.join(root, file)
                new_file = file.replace(pattern, replacement)
                new_path = os.path.join(root, new_file)
                os.rename(old_path, new_path)
                print(f"Renamed: {old_path} → {new_path}")

# (d) Move files by extension
def move_files_by_extension(directory):
    ext_dirs = {
        ".pdf": os.path.join(directory, "PDF_Files"),
        ".txt": os.path.join(directory, "TXT_Files"),
        ".xlsx": os.path.join(directory, "Excel_Files"),
    }
    for folder in ext_dirs.values():
        os.makedirs(folder, exist_ok=True)

    for root, dirs, files in os.walk(directory):
        for file in files:
            src_path = os.path.join(root, file)
            ext = os.path.splitext(file)[1]
            if ext in ext_dirs:
                dest_path = os.path.join(ext_dirs[ext], file)
                shutil.move(src_path, dest_path)
                print(f"Moved: {file} → {ext_dirs[ext]}")

# (e) Calculate total size of a directory
def calculate_directory_size(directory):
    total_size = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            total_size += os.path.getsize(os.path.join(root, file))
    print(f"\nTotal size of '{directory}': {total_size/1024:.2f} KB")
    return total_size

# --- Demo ---
if __name__ == "__main__":
    create_directory_structure()
    list_files_recursively(BASE_DIR)
    rename_files_pattern(BASE_DIR, pattern="draft", replacement="final")
    move_files_by_extension(BASE_DIR)
    calculate_directory_size(BASE_DIR)