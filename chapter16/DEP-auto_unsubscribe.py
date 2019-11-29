#! /usr/bin/python3

# auto_unsubscribe.py - A program to automatically bring up all unsubscribe buttons present in your yahoo email inbox.

# Usage: ./auto_unsubscribe.py <credentials>
# where <credentials> is a text file, the first line being username@yahoo.com and the second line being app-specific password from yahoo.

# Import modules
import sys, imtp, bs4

# Read in email credentials
try:
	f = open(sys.argv[1], 'r')
	username = f.readline()
	password = f.readline()
	f.close()

except:
	print("Credentials could not be found or read.")
	exit()

# TODO Establish IMAP connection
# TODO Download messages
# TODO Close IMAP connection
# TODO Loop through downloaded messages
# TODO Search for unsubscribe href/link
# TODO When link is found, open web browser pointing to the unsubscribe url
