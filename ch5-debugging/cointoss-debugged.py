# Fixed: guess was compared to toss as a str vs int, which always means False here. heads_tails_comparison() converts guess to match toss's 1/0 encoding before comparing.

import random

toss = random.randint(0, 1)  # 0 is tails, 1 is heads
guess = ''

def heads_tails_comparison(guess):
    if guess == 'heads':
        guess = 1
    elif guess == 'tails':
        guess = 0
    return guess

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

guess = heads_tails_comparison(guess)


if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    guess = heads_tails_comparison(guess)

    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
