#! /usr/bin/python3

# text_me.py - Defines a function for texting a message to my personal phone number.
# Usage: from text_me import text_me; text_me('string message to be sent via sms')

# Import modules
import os
from twilio.rest import Client

def text_me(text):

	# Get email & password from text file
	f = open('/home/austin/twilio.txt','r')
	acct_sid = f.readline().rstrip()
	auth_token = f.readline().rstrip()
	twilio_number = f.readline().rstrip()
	my_number = f.readline().rstrip()
	f.close()

	# Establish connection to Twilio server
	client = Client(acct_sid, auth_token)

	# Send message
	client.messages.create(body = text, from_ = twilio_number, to = my_number)

	return 0
