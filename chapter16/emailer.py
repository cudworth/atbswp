#! /usr/bin/python3

# emailer.py - A program to automatically send email messages. (DEP)

# Import modules
import smtplib, sys

# Get email & password from text file
f = open('/home/austin/email.txt','r')
email = f.readline().rstrip()
password = f.readline().rstrip()
f.close()

# Set recipient address
# recipient = '8168320060@tmomail.net'
recipient = 'austincudworth@gmail.com'

# Establish email server connection
host = 'smtp.mail.yahoo.com'
port = '465'
server = smtplib.SMTP_SSL(host, port)
server.login(email, password)

# Build message
msg = 'Subject: hello world\n\n Body text here'

# Send mail
server.sendmail(email, recipient, msg)

# Disconnect from email server
server.quit()
