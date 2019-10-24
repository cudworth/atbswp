#! /usr/bin/python3

# 2048.py - Program to automatically play the game '2048' in a web browser

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Initialize web browser
ff = webdriver.Firefox()

# Open 2048 game at the following url
url = 'https://gabrielecirulli.github.io/2048/'
ff.get(url)
page = ff.find_element_by_tag_name('html')

# While gameover element does not exist,
while len(ff.find_elements_by_tag_name('div.game-message.game-over')) == 0:

	# Send URDL keystroke pattern to the game
	page.send_keys(Keys.UP)
	page.send_keys(Keys.RIGHT)
	page.send_keys(Keys.DOWN)
	page.send_keys(Keys.LEFT)

# Find score element
score = ff.find_element_by_class_name('score-container').text

# Do use primary score only, sometimes find_element captures additive points
score = score.split('\n')[0]

# Report score achieved
print('Final score: %s points' %score)

# Close web browser
ff.close()
