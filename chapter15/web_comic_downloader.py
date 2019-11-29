#! /usr/bin/python3
# web_comic_downloader.py - A program to download the latest comics at XKCD

# Import modules
import os, shelve, requests, bs4

# Working directory and log file names
directory = 'comics'
log_file = 'log'

# Make working directory if it does not exist
os.makedirs(directory, exist_ok = True)

# Open webpage
url = 'https://www.xkcd.com/'
page = requests.get(url)

# Create soup
soup = bs4.BeautifulSoup(page.text)

# Find comic element
elem = soup.find('div', id='comic').find('img')

# Get title, link, etc.
title = elem.get('title')
alt = elem.get('alt')
src = elem.get('src')

# Format filenames based on site info
image_filename = src.split('/')[-1]
basename, extension = os.path.splitext(image_filename)
caption_filename = basename + '.txt'

# Generate url for image file
url = 'http:' + src

# Load download log
shelf = shelve.open(os.path.join(directory, log_file))

try:
	# Try to open list of comics previously downloaded
	comics = shelf['comics']

except KeyError:

	# If list of comics does not exist
	comics = []

# If comic has not yet been downloaded
if title not in comics:

	# Let user know a new comic was found
	print(f'New comic \'{alt}\' was found.')

	# Download image file from web
	img = requests.get(url)
	img.raise_for_status

	# Open image file
	f = open(os.path.join(directory, image_filename), 'wb')

	# Write image file
	for chunk in img.iter_content(100000):
		f.write(chunk)

	# Close image file
	f.close()

	# Open text file
	f = open(os.path.join(directory, caption_filename), 'w')
	
	# Write text file
	f.write(alt + '\n'*2)
	f.write(title + '\n')

	# Close text file
	f.close()

	# Add title to list of comics
	comics.append(title)

	# Update shelf log
	shelf['comics'] = comics

else:
	print('No new comics were found, exiting now.')

# Close shelf file
shelf.close()
