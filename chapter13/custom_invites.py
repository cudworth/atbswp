#! /usr/bin/python3
# custom_invites.py - Takes a text file containing a list of names and creates a sequence of invitation pages within a MS word document for easy printing.
# Usage: custom_invites.py <guestlist>
# Reads a text file <guestlist> line by line, and adds each line to a prepared invitation

# Import modules
import sys, os, docx

# Parse user input
if len(sys.argv) == 2 and os.path.exists(sys.argv[1]):
	guest_list = sys.argv[1]
else:
	print('Improper usage')
	exit()

# Open and read guestlist text file
f = open(guest_list,'r')
lines = f.readlines()

# Open word document
doc = docx.Document('invitations.docx')


# Loop through guest list
for line in lines:

	# Remove newline char
	line = line.rstrip('\n')

	# Add new invitation page & substitute a name from the guestlist
	doc.add_paragraph('It would be a pleasure to have the company of').style = 'User Index 1'
	doc.add_paragraph(line).style = 'User Index 2'
	doc.add_paragraph('at 1100 Memory Lane on the Evening of').style = 'User Index 1'
	doc.add_paragraph('April 1st').style = 'User Index 2'
	doc.add_paragraph('at 7 o\'clock').style = 'User Index 1'

	# Add page break
	doc.add_page_break()

# Save document
filename = '_' + 'invitations.docx'
doc.save(filename)


