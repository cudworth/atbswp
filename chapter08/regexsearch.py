#! Python3
# regexsearch.py - Reads text files in CWD and returns results for REGEX 
# Usage: python3 regexsearch.py <'REGEX'>

import sys, re, os

if len(sys.argv) == 1:
	# Prompt user to input a regex query
	arg = input('\nProvide regex pattern:\n')
	RO = re.compile(r'' + arg)

if len(sys.argv) == 2:
	# Use provided pattern in regex query
	RO = re.compile(r'' + sys.argv[1])

for item in os.listdir():

	if item[-4:] == '.txt': # Test for .txt file

		FO = open(item) # Open the .txt file

		lines = FO.readlines() # Read lines from text file

		FO.close() # Close the file once it has been read

		for line in lines:

			MO = RO.search(line)
			
			if MO: # If a match object is found, print the file and line inclusive of the search term

				print('\nMatch found in file ' + item + ':')
				print(line)
