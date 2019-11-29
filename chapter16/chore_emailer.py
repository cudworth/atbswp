#! /usr/bin/python3

# chore_emailer.py - A program to automatically assign chores to various people via email.

# Import modules
import smtplib, getpass, random

# Create chore-email pairs
chores = ['garbage','vacuum','sweep','dust','dishes','mop','toilets','shower','windows','tidy','shoes']

emails = [	'austincudworth@gmail.com',
		'austincudworth@yahoo.com']

# Initialize dict of assignments
assigns = {}
for email in emails:
	assigns[email] = []

# Randomly select starting email
email_index = random.randint(0, len(emails) - 1)

# Loop while chores are not completely assigned
while 0 < len(chores):

	# Randomly select a chore
	chore_index = random.randint(0, len(chores) - 1)

	# Get string value for chore and remove from list of chores
	chore = chores.pop(chore_index)

	# Assign the random chore to an email
	assign = assigns[emails[email_index]]
	assign.append(chore)
	assigns[emails[email_index]] = assign

	# Increment to next email
	email_index += 1
	if email_index == len(emails):
		email_index = 0

# Sign into email server
host = 'smtp.mail.yahoo.com'
port = '465'
user = 'austincudworth@yahoo.com'
password = getpass.getpass()
so = smtplib.SMTP_SSL(host)
so.login(user, password)

# Loop through chore-email pairs in assigns dictionary
for recipient, chores in assigns.items():

	# Build string list of chores separated w/ newline chars
	chores = ', '.join(chores)

	# Build email message
	msg = r'Subject: Chore Assignments: ' + chores

	# Send email to each recipient w/ chores assigned
	so.sendmail(user, recipient, msg)	

# Disconnect from email server
so.quit()
