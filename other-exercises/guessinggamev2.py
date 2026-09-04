import random

random_number = random.randint(1,50)

def guessing_sequence(user_guess):
    if user_guess > random_number:
        user_guess = int(input('User-provided guess is greater than the random number. Pick a lower number: '))
    elif user_guess < random_number:
        user_guess = int(input('User-provided guess is lower than the random number. Pick a higher number: '))
    return user_guess

user_guess = int(input('Please enter a random number between 1 and 50: '))

while user_guess != random_number:
    user_guess = guessing_sequence(user_guess)

print(f'You have guessed the correct random number: {random_number}. Congratulations!')
