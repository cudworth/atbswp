#! /usr/bin/python3

# link_verification.py - Program to download all pages linked from given home page.
# Usage: link.verification.py <url>
# Program downloads all links found on page located at <url> and reports all broken links found.

import os, sys, requests, bs4

# Function to switch between http and https
def http_switch(url):
	if url[:5] == 'https':
		url = 'http' + url[5:]
	else:
		url = 'https' + url[4:]
	return url	

# Verify input arguments are provided
if len(sys.argv) != 2:
	print('Improper usage')
	exit()
else:
	url = sys.argv[1]

# Lop off trailing '/' if exists
if url[-1] == '/':
	url = url[:-1]

# Request source webpage
page = requests.get(url)
page.raise_for_status()

# Find all links on the page
soup = bs4.BeautifulSoup(page.text,features="lxml")
links = soup.find_all(href=True)

# Sequentially loop thorugh each link and attempt to request the linked page
for link in links:
	link_url = link.get('href')

	if link_url[:2] == '//': # If link is not actually relative but w/o http specified
		link_url = 'http:' + link_url

	elif link_url[:4] != 'http': # If link is relative to original page
		link_url = url + link_url

	try:
		requests.get(link_url).raise_for_status()
	except:
		try:
			requests.get(http_switch(link_url)).raise_for_status()
		except:
			print('Broken link: %s' %link_url)
