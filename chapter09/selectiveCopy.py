#! /usr/bin/python3
# selectiveCopy.py - This program walks through a folder tree and searches
# for files with a user input file extension. These files are then copied
# from their existing location to a new folder.

# Usage: selectiveCopy.py <extension> <destination>

import os, sys, shutil, re

# Verify enough arguments have been provided
if len(sys.argv) != 3:
	print('Not enough arguments provided.')
	quit()		

# Regex for file extension provided by the user
RO = re.compile(r"""^(.*)(\."""
		+ sys.argv[1].upper()
		+ """)$""", re.VERBOSE | re.IGNORECASE)

# Verify destination folder exists and if not, create one
destination = os.path.join(os.getcwd(),sys.argv[2])

if not os.path.isdir(destination):

	os.mkdir(destination)

	print('Created folder at destination:\n'+destination)

else:
	print('Destination folder found on drive')

# Walk through folder identifying files with matching extensions
for dirpath, dirnames, filenames in os.walk(os.getcwd()):

	# Do not make copies of files already in the destination folder
	if dirpath == destination:
		continue

	# Search filenames and copy regex matched files to destination
	for filename in filenames:

		if RO.match(filename):

			print('Copying %s into directory %s' %(filename, destination))
			shutil.copy(os.path.join(dirpath,filename),destination)
