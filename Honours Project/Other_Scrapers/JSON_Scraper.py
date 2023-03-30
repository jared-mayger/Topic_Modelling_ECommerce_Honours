import os
import shutil

# Define the directory where your files are located
directory = '/Users/jaredmayger/Desktop/Honours Project/'

# Create the directories where you want to move your files
image_dir = os.path.join(directory, 'images_final')
txt_dir = os.path.join(directory, 'txt_docs')
zip_dir = os.path.join(directory, 'zipped_files')

# Loop through all the files in the directory
for file in os.listdir(directory):
    # Get the file extension
    ext = os.path.splitext(file)[1]
    
    # Move the file to the appropriate directory based on its extension
    if ext == '.jpg':
        shutil.move(os.path.join(directory, file), image_dir)
    elif ext == '.txt':
        shutil.move(os.path.join(directory, file), txt_dir)
    elif ext == '.xz':
        shutil.move(os.path.join(directory, file), zip_dir)