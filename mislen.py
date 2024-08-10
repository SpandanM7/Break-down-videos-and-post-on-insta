import os

folder_path = "target"

# List all files and directories in the folder
all_files = os.listdir(folder_path)

# Count only files
file_count = sum(1 for file in all_files if os.path.isfile(os.path.join(folder_path, file)))

print(f"Number of files: {file_count}")
