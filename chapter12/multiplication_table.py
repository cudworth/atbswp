#! /usr/bin/python3

# Take a number from the command line and creates a multiplication table
# embedded in an excel spreadsheet.

# Usage: multiplication_table.py <N>
# Creates a multiplication table N x N within an Excel spreadsheet and saves the file to disk.

# Import modules
import sys, os, openpyxl
from openpyxl.utils import get_column_letter as g_c_l

# Check for adequate inputs
if len(sys.argv) != 2:
	print('Improper usage')
	exit()

# Set argument to N
try:
	N = int(sys.argv[1])
except:
	print('Improper usage')
	exit()

# Open spreadsheet object for editing
workbook = openpyxl.Workbook()
sheet = workbook.active

# Loop through each cell to evaluate and set multiplication values
for row in range(1, N + 1):

	for col in range(1, N + 1):

		cell = g_c_l(col + 1) + str(row + 1) # Determine string formatted cell name
		sheet[cell] = row * col # Set cell value to matrix value

# Set format for column/row headers
style = openpyxl.styles.Font(bold=True)

# Insert row titles
for row in range(1, N + 1):
	cell = 'A' + str(row + 1)
	sheet[cell] = row
	sheet[cell].font = style

# Insert column titles
for col in range(1, N + 1):
	cell = g_c_l(col + 1) + '1'
	sheet[cell] = col
	sheet[cell].font = style

# Write changes and close spreadsheet
workbook.save('outfile.xlsx')
