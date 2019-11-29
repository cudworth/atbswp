#! /usr/bin/python3

# umbrella_reminder.py - A program to check the weather and issues a text message if the weather calls for an umbrella.

# Import modules
import requests, bs4, re
from text_me import text_me

# Load weather page
url = 'https://forecast.weather.gov/MapClick.php?lat=47.640930000000026&lon=-122.27713499999999'
page = requests.get(url)
page.raise_for_status()

# Create soup
soup = bs4.BeautifulSoup(page.text, features = 'lxml')

# Locate weather report for today
weather = soup.find('div', class_='col-sm-10 forecast-text').text

# Compile regex to search for rain in today's forecast
ro = re.compile(r'(rain|snow|drizz|shower|mist|precip)', re.IGNORECASE)

# If precipitation is forecast, send sms notifier
if ro.search(weather):

	print('Precipitation is in the forecast, sending text message.')
	text_me('Pack an umbrella today!')
