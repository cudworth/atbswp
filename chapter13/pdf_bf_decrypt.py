#! /usr/bin/python3
# pdf_bf_decrypt.py - Attempts to unlock a user specified pdf file, checking passwords against single words included in dictionary.txt
# Usage: pdf_bf_decrypt.py <pdf_file>

# Import modules
import sys, os, PyPDF2

# Accept input args
if len(sys.argv) == 2 and os.path.exists(sys.argv[1]):
	pdf_file = sys.argv[1]
else:
	print('Improper usage')
	exit()

# Read in english dictionary
f = open('dictionary.txt','r')
lines = f.readlines()
f.close()

# Initialize list of words
dictionary = []

# Loop through lines of dictionary
for line in lines:

	word = line.rstrip() # Remove trailing whitespace

	# Create caps/lower/upper versions of each word
	dictionary.append(word.lower())
	dictionary.append(word.upper())
	dictionary.append(word.title())

# Open pdf file
f = open(pdf_file, 'rb')
pdf = PyPDF2.PdfFileReader(f)

# Loop through words in dictionary
for word in dictionary:
	if pdf.decrypt(word):
		print('Password \'%s\' unlocked the target file.' % word)
		break

# Close file
f.close()
