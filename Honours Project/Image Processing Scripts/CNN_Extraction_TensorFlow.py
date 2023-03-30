import tensorflow as tf
import keras as keras
from keras.applications.vgg16 import VGG16
from keras.preprocessing.image import load_img, img_to_array
import os
import numpy as np

# Load the pre-trained VGG16 model
model = VGG16(weights='imagenet', include_top=False)

# Define a function to extract features from an image using the VGG16 model
def extract_features(filename):
    # Load the image
    img = load_img(filename, target_size=(224, 224))
    # Convert the image to a numpy array
    img_array = img_to_array(img)
    # Expand the dimensions of the image to match the input dimensions of the VGG16 model
    img_array = tf.keras.applications.vgg16.preprocess_input(img_array)
    # Extract features using the VGG16 model
    features = model.predict(img_array.reshape((1, img_array.shape[0], img_array.shape[1], img_array.shape[2])))
    return features.reshape(7*7, 512)

# Define the input and output folders
input_folder = '/Users/jaredmayger/Desktop/Honours Project/Dataset_Images_Resized'
output_folder = '/Users/jaredmayger/Desktop/Honours Project/Dataset_Image_Features'

# Create the output folder if it doesn't already exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through each file in the input folder, extract features, and save the results to the output folder
for filename in os.listdir(input_folder):
    # Extract features
    features = extract_features(os.path.join(input_folder, filename))
    # Save features to file
    np.savetxt(os.path.join(output_folder, filename.split('.')[0] + '.txt'), features)
