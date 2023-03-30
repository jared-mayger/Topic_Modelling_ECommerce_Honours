from PIL import Image
import os

# Set the input and output directories
input_dir = '/Users/jaredmayger/Desktop/Honours Project/Dataset_Images_Initial'
output_dir = '/Users/jaredmayger/Desktop/Honours Project/Dataset_Images_Resized'

# Set the desired image size
size = (256, 256)

# Loop through all the image files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.jpg'):
        # Load the image
        image_path = os.path.join(input_dir, filename)
        image = Image.open(image_path)

        # Resize the image
        image = image.resize(size)

        # Save the resized image to the output directory
        output_path = os.path.join(output_dir, filename)
        image.save(output_path)