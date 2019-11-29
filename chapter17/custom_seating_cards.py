#! /usr/bin/python3
# custom_invites.py - Takes a text file containing a list of names and creates a set of seating card images
# Usage: custom_seating_cards.py <guestlist>
# Reads a text file <guestlist> line by line, and adds each line to a prepared invitation

# Import modules
import sys, os
from PIL import Image, ImageDraw, ImageFont

# Font location
font_location = '/usr/share/fonts/truetype/dejavu'

os.makedirs('invites', exist_ok = True)

# Parse user input
if len(sys.argv) == 2 and os.path.exists(sys.argv[1]):
	guest_list = sys.argv[1]
else:
	print('Improper usage')
	exit()

# Open and read guestlist text file
f = open(guest_list,'r')
lines = f.readlines()

ppi = 72 # Typical pixels per inch for output file type
card_w = 5 * ppi # Desired card width in pixels
card_h = 4 * ppi # Desired card height in pixels

# Open image document
img = Image.open('cherry.png')

w, h = img.size

# Determine a scale to use
if w/card_w < h/card_h:
	scale = w/card_w

else:
	scale = h/card_h

# Scale the image
img = img.resize((int(w/scale), int(h/scale)))

# Determine new image size
w, h = img.size

# Calculate padding in width or height of image
w_pad = (w - card_w) / 2
h_pad = (h - card_h) / 2

# Calculate crop box extents
x1 = 0 + w_pad
y1 = 0 + h_pad
x2 = w - w_pad
y2 = h - h_pad

# Crop image to desired dimensions
crop_box = (x1,y1,x2,y2)
img = img.crop(crop_box)

# Create ImageDraw object
draw = ImageDraw.Draw(img)

# Draw a black rectangle outline for easy cutout
draw.rectangle((0, 0, card_w - 1, card_h - 1), outline='black')

# Create font object
font_ = ImageFont.truetype(os.path.join(font_location,'DejaVuSans-Bold.ttf'), size = 28)

# Loop through invitations
for line in lines:
	
	# Create copy of base image
	invite = img.copy()
	draw = ImageDraw.Draw(invite)

	# Remove newline char
	line = line.rstrip('\n')

	# Get size of text
	w, h = draw.textsize(line, font = font_)

	# Calculate padding
	x1 = (card_w - w) / 2
	y1 = (card_h - h) / 2

	# Draw text
	draw.text((x1, y1), line, fill = 'black' ,font = font_)

	# Save image
	invite.save(os.path.join('invites', f'{line}.png'))
