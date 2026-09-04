import random

random_number = random.randint(1,50)

def guessing_sequence(user_guess):
    if int(user_guess) > int(random_number):
        user_guess = input('User-provided guess is greater than the random number. Pick a lower number: ')
        user_guess = int(user_guess)
    elif int(user_guess) < int(random_number):
        user_guess = input('User-provided guess is is lower than the random number. Pick a higher number: ')
        user_guess = int(user_guess)
    return int(user_guess)

user_guess = input('Please enter a random number between 1 and 50: ')
user_guess = int(user_guess)

while user_guess != random_number:
    user_guess = guessing_sequence(user_guess)

print(f'You have guessed the correct answer of {random_number}. Congrats!')
