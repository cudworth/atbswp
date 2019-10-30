#! /usr/bin/python3

# text_files_to_spreadsheet.py

# A program to read user specified text files and write individual lines to columns in a spreadsheet.

# Usage: text_files_to_spreadsheet.py <file1> <file2> <file3>...

# Import modules
import os, sys, openpyxl
from openpyxl.utils import get_column_letter as g_c_l

# Parse inputs
try:
	filenames = sys.argv[1:]
except:
	print('Improper usage')
	exit()

# Verify filenames provided
for filename in filenames:
	assert os.path.exists(filename), 'File %s could not be found' % filename

# Open a spreadsheet
workbook = openpyxl.Workbook()
sheet = workbook.active

# Loop through files
for i in range(len(filenames)):

	# Open and read lines from text file
	f = open(filenames[i])
	lines = f.readlines()
	f.close()

	# Determine column letter for a given filename
	col = g_c_l(i + 1)

	# Loop through lines and update corresponding cell value
	for j in range(len(lines)):
		cell = col + str(j + 1)
		sheet[cell] = lines[j]

# Save and close the workbook
workbook.save('combined.xlsx')
workbook.close()




	
