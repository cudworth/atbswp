#! /usr/bin/python3
# pdf_encrypt.py - A program to encrypt all pdf files within a given directory
# Usage: pdf_encrypt.py <directory> <password> encrypt all pdf files found within <directory> with provided <password>

# Import modules
import os, sys, PyPDF2

# Parse user input
if len(sys.argv) == 3 and os.path.exists(sys.argv[1]):
	root_dir = sys.argv[1]

else:
	print('Improper usage')
	exit()

# Set password to user provided string
password = sys.argv[2]

# Walk file directory
for dirpath, dirnames, filenames in os.walk(root_dir):

	# Loop through files
	for filename in filenames:

		# Create absolute path to file
		filename_abs = os.path.join(dirpath, filename)

		# Check to see if file has pdf extension
		if filename_abs.upper().endswith('.PDF'):

			# Read original pdf object
			fi = open(filename_abs, 'rb')
			pdf_in = PyPDF2.PdfFileReader(fi)

			# Check to see if file is already encrypted
			if pdf_in.isEncrypted:
				fi.close()
				print('File %s is already encrypted.' % filename_abs)
				continue

			# Initialize new pdf object
			pdf_out = PyPDF2.PdfFileWriter()

			# Loop through pages of pdf_in and add to pdf_out
			for i in range(pdf_in.getNumPages()):
				pdf_out.addPage(pdf_in.getPage(i))

			# Encrypt the file
			pdf_out.encrypt(password)

			# Write encrypted file
			new_file = os.path.join(dirpath, '_enc__' + filename)
			fo = open(new_file, 'wb')
			pdf_out.write(fo)

			# Close opened files
			fi.close()
			fo.close()



