#! /usr/bin/python3

# fillGaps.py -
# Write a program that finds all files with a given
# prefix, such as spam001.txt, spam002.txt, and so
# on, in a single folder and locates any gaps in
# the numbering (such as if there is a spam001.txt
# and spam003.txt but no spam002.txt). Have the
# program rename all the later files to close this gap.

# Usage: fillagaps.py <directory> <prefix>

import os, re, sys, shutil

# Verify <directory> and correct number of arguments provided
if len(sys.argv) == 3 and os.path.isdir(sys.argv[1]):
	pass
else:
	print('Incorrect usage')
	exit()

# Compile regex to locate sequential files and store filenames & sequence number
RO = re.compile(r'''^('''
		+ sys.argv[2] +
		r''')(\d+)(.*)$''', re.VERBOSE)

seq = []
i = 0


for filename in os.listdir(os.path.abspath(sys.argv[1])):

# Find matches and compile a sequence list, along w/ prefix, suffix, and num
	if RO.match(filename):

		[pre, num, suf] = RO.match(filename).groups()
		seq.append(int(num))
		chars = len(num)

# Sort file sequence no.
seq.sort()

# Start counter at lowest sequence number found
i = min(seq)

# Loop through each item in sequence and check to make sure files increment by one each loop
# If not, the existing file is moved w/ filename corresponding to an increment of one.
for item in seq:
	if item == i:
		i += 1
		pass
	else:
		old_file = os.path.join(os.path.abspath(sys.argv[1]),pre+str(item).zfill(chars)+suf)
		new_file = os.path.join(os.path.abspath(sys.argv[1]),pre+str(i).zfill(chars)+suf)
		shutil.move(old_file, new_file)		
		i += 1
