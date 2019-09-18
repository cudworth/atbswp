#!Python3

def collatz(number):
	'''Collatz sequence function
	if number is even, perform integer division
	if number is odd, return 3 * number + 1.
	'''

	if number % 2 == 0:
		return number // 2
	else:
		return 3 * number + 1

mynumber = input('\nEnter a number to generate a collatz sequence:\n\n')

try:
	mynumber = int(mynumber)

	while mynumber != 1: #Proceed to call collatz function until return value is equal to 1.
		mynumber = collatz(mynumber)
		print(mynumber)

except:
	print('\nNon-integer entry, please try again.\n')


