#! /usr/bin/python3
# Austin Cudworth, 10/14/19

# coin_toss.py - Player gets two guesses

import random, logging

logging.basicConfig(filename = 'coin_toss_log.txt', level=logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')

guess = ''

while guess not in ('heads', 'tails'):
	print('Guess the coin toss! Enter heads or tails:')
	guess = input()

toss = random.randint(0, 1) # 0 is tails, 1 is heads

logging.debug('Coin state is %s' %toss)

if guess == 'tails' and toss == 0 or guess == 'heads' and toss == 1:
	print('You got it!')

else:
	print('Nope! Guess again!')
	guess = input()

	if guess == 'tails' and toss == 0 or guess == 'heads' and toss == 1:
		print('You got it!')

	else:
		print('Nope. You are really bad at this game.')
