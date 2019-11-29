#!/usr/bin/python3
#find_photo_folders.py - Program to locate photo folders on a disk drive

# Import modules
import os
from PIL import Image

directory = '/home/austin/Dropbox'
min_size = 300 # Minimum image recognized to be considered a photo
threshold = 1/2 # Fraction of folder that must be image files to be considered a photo folder

extensions = ('jpg','bmp','img','png','gif') # File extensions recognized as images

# Loop through directories
for (dirpath, dirnames, filenames) in os.walk(directory):

    # Set counter to zero for each folder walked through
    img_count = 0

    # Loop through files
    for filename in filenames:

        # Get file extension
        extension = filename[-3:].lower()

        # Check to see if extension matches those for recognized image files
        if extension in extensions:
            
            try:
                # Open image and get dimensions
                img = Image.open(os.path.join(dirpath,filename))
                (width, height) = img.size

                # Check if image exceeds minimum size
                if min_size < width and min_size < height:

                    # Increment image counter
                    img_count += 1

            except:
                # Print an error message
                print(f'File: {os.path.join(dirpath,filename)} could not be accessed with PIL\n')
    
    # If fraction of photos in folder exceed the threshold, indicate a photo folder has been found
    if 0 < len(filenames) and threshold < img_count/len(filenames):

        print(f'Photo folder found: {dirpath}\n')
