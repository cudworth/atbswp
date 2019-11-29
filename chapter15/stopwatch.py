#! /usr/bin/python3
# stopwatch.py - A stopwatch program written in python.

# Import modules
import time

input('Press Enter to start the stopwatch.')
print('Press Ctrl+C at any time to close the stopwatch')

# Initialize the stopwatch 
lap_num = 0
start = time.time()
lap = start

# Loop until broken
while True:

	try:

		# Wait for the return key to be pressed
		input()

	except KeyboardInterrupt:

		# Close out when keyboard interrupt is received
		print('\nExiting stopwatch')
		exit()

	# Increment lap number
	lap_num += 1

	# Record split time
	split = time.time() - lap

	# Current lap time
	lap += split

	# Calc elapsed time
	elapsed = lap - start

	# Format vars for printing
	p_lap_num = str(lap_num).rjust(2)
	p_split = str(round(split, 1)).rjust(5)
	p_elapsed = str(round(elapsed, 1)).rjust(5)

	# Print stopwatch results
	print(f'Lap #{p_lap_num} {p_elapsed} ({p_split})', end = '')
