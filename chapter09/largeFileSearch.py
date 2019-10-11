#! /usr/bin/python3

# largeFileSearch.py - Walk through folder tree identifying
# files of size greater than 100MB

# Usage: largeFileSearch <directory> <size>
# searches the listed <directory> for files exceeding 100MB. 
# Defaults to searching the current working directory if 
# none is provided by the user.

import os, sys

# Check for user input, determine starting directory
if len(sys.argv) == 2 and os.path.isdir(sys.argv[1]):

	topdir = os.path.abspath(sys.argv[1])

else:

	topdir = os.getcwd()

# Set filesize lower limit
limit = 100*10**6 #Bytes

# Walk the directory tree
for dirpath, dirnames, filenames in os.walk(topdir):

	for filename in filenames:

		# Verify the file is a file and not a link
		if os.path.isfile(os.path.join(dirpath,filename)):

			# If filesize exceeds lower limit, print file with absolute path 
			if os.path.getsize(os.path.join(dirpath,filename)) > limit:

				fsize = str(os.path.getsize(os.path.join(dirpath,filename))/(10**6))
				print(os.path.join(dirpath,filename),end='')
				print(' (',end = '')
				print(fsize + ' MB)')
