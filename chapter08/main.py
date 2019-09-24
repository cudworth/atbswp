#! Python3

'''
Chapter 08 practice problems
'''

'''
-Madlibs program-
Read in a text file and offer
to replace existing adjectives, nouns, adverbs and verbs
with user input.
'''

import re

RO = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')

prompts = {
	'ADJECTIVE':'\nEnter an adjective:\n',
	'NOUN':     '\nEnter a noun:\n',
	'ADVERB':   '\nEnter an adverb:\n',
	'VERB':     '\nEnter a verb:\n'
	}

readfile = open('./chapter08/madlib.txt','r')
txt = readfile.read()
readfile.close()

match = RO.search(txt)

while match:

	rtext = input(prompts[match.group()])

	txt = RO.sub(rtext,txt,1)

	match = RO.search(txt)

print(txt)

writefile = open('./chapter08/madlib.txt','w')
writefile.write(txt)
writefile.close()
