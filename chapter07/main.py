#!Python3

'''
Chapter 07 practice problems
Austin Cudworth, 9/20/19
'''

'''
-Strong Password Detection-
'''

def passCheck(passwd):

	# (8) characters min & contains uppercase letters, lowercase letters, and numbers
	
	import re
	
	t0 = re.compile(r'[a-zA-Z0-9]{'+str(len(passwd))+'}')
	t1 = re.compile(r'[a-z]')
	t2 = re.compile(r'[A-Z]')
	t3 = re.compile(r'[0-9]')

	valid = False

	if len(passwd) >= 8:

		if t0.search(passwd):

			if t1.search(passwd):

				if t2.search(passwd):

					if t3.search(passwd):

						valid = True

	if valid:

		print('PASSWORD \'' + passwd + '\' ACCEPTED')

	else:

		print('PASSWORD \'' + passwd + '\' REJECTED') 

passCheck('2Short')
passCheck('$pecialCharacters123')
passCheck('ALLCAPS123')
passCheck('alllowercase123')
passCheck('nodigits')
passCheck('GoodPass123')


'''
Regex version of strip method
'''

def customStrip(string,*chars):

	'''
	Function to strip any leading or trailing
	whitespace. If chars are passed to the
	function, any leading or trailing chars
	are stripped from the string.
	'''
	
	import re

	try:
		regchar = chars[0]

	except:
		regchar = r'\s'	
 
	LRO = re.compile(r'^['+regchar+r'\s]+') # Regex object for leading chars
	TRO = re.compile(r'['+regchar+r'\s]+$') # Regex object for trailing chars

	LMO = LRO.search(string) # Match object for leading chars
	TMO = TRO.search(string) # Match object for trailing chars

	if LMO != None:
		LD = len(LMO.group()) # Leading digits to strip from input string
		string = string[LD:]

	if TMO != None:
		TD = len(TMO.group()) # Trailing digits to strip from input string
		string = string[:-TD]
	
	return string

print(customStrip('     test w/ leading space'))
print(customStrip('test w/ trailing space    '))
print(customStrip('  test w/ space @ ends    '))
print(customStrip('----test w/ - chars--', '-'))























