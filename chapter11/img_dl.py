#! /usr/bin/python3

# img_dl.py - Program that downloads the first few images found on Imgur for the search term provided. Images are saved to a new folder in the current directory.
# Usage: img_dl <quantity> <search terms>

import os, sys, requests, bs4
from selenium import webdriver

# Build search terms from input arguments
assert len(sys.argv) > 2, 'Improper usage' 
qty = int(sys.argv[1])
query = ' '.join(sys.argv[2:])

# Create folder based on search terms
path = os.path.abspath(query)
if os.path.exists(path) == False:
	os.mkdir(path)

# Build search url for Imgur
root = 'http://imgur.com'
url = root + '/search?q=' + query

# Use requests & bs4 to process search results
page = requests.get(url)
page.raise_for_status()
soup = bs4.BeautifulSoup(page.text)
items = soup.find_all('a', class_='image-list-link')

# Processed image counter
i = 0

# Open selenium browser
ff = webdriver.Firefox()
ff.implicitly_wait(6)

# Loop through search results sequentially
for item in items:

	# Visit linked page for each search result
	url = root + item.get('href')
	ff.get(url)

	# Find div.image that has been loaded
	elements = ff.find_elements_by_css_selector('div.image')

	# Loop through each div.image on the page	
	for element in elements:

		# Find src/url for image file
		try:
			imgurl = element.find_element_by_tag_name('img').get_attribute('src')

		except:
			continue

		# Obtain filename for the image from url	
		filename = imgurl.split('/')[-1]

		# Filter for image filetypes only
		if filename[-3:].lower() not in ('jpg','bmp','png'):
			continue

		# Request image file from the server
		img = requests.get(imgurl)
		img.raise_for_status()

		# Write image file to disk in the new directory
		f = open(os.path.join(path, filename), 'wb')
		for chunk in img.iter_content(100000):
			f.write(chunk)
		f.close()

		# Increment count of images processed
		i += 1

		# Stop searching once qty images has been met
		if i == qty:
			ff.close()
			quit()

if i != qty:
	ff.close()
	print('Insufficient number of images found in search results')


