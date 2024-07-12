import os
import shutil

# Define the source and destination directories
source_dir = 'markdown'
destination_dir = 'input'

# Create the destination directory if it doesn't exist
os.makedirs(destination_dir, exist_ok=True)

# Walk through the source directory
for root, dirs, files in os.walk(source_dir):
    for file in files:
        if file.endswith('.md'):
            # Construct the full file path
            file_path = os.path.join(root, file)
            # Copy the file to the destination directory
            shutil.copy2(file_path, destination_dir)
            print(f'Copy: {file_path} to {destination_dir}')

print('All .md files have been copied.')

