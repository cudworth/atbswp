#! /usr/bin/python3

# cl_emailer.py - Program to send a string of text to a specified email address
# from an existing Protonmail address.

# Usage: cl_emailer <username> <password> <recipient@domain.com> <messages> 

import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

try:
	user_name = sys.argv[1]
	password = sys.argv[2]
	recipient = sys.argv[3]
	body = ' '.join(sys.argv[4:])

except:
	print('Improper usage')
	quit()

# Define throwaway account name and domain
subject = 'Automated email, do not reply'

# Open a browser window
br = webdriver.Firefox()
br.implicitly_wait(10)
br.get('https://mail.protonmail.com/login')

# Login to email client
path = '//*[@id="username"]'
br.find_element_by_xpath(path).send_keys(user_name)

path = '//*[@id="password"]'
br.find_element_by_xpath(path).send_keys(password)

path = '//*[@id="login_btn"]'
br.find_element_by_xpath(path).click()

# Compose email
path = '/html/body/div[2]/div[1]/section/button'
br.find_element_by_xpath(path).click()

# Specify recipient email address
name = 'autocomplete'
br.find_element_by_name(name).send_keys(recipient)

# Fill body and subject of email
css_selector = 'input.flex'
br.find_element_by_css_selector(css_selector).send_keys(subject)

path = '/html/body/div[1]'
br.find_element_by_xpath(path).send_keys(body)

# Send email
path = '/html/body/div[2]/form[1]/div/footer/div/button[3]'
br.find_element_by_xpath(path).click()

# Close out of browser window
