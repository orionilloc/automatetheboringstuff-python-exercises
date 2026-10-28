# Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file. For example, a text file may look like this:

# The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.

# The program would find these occurrences and prompt the user to replace them:

#Enter an adjective:
#silly
#Enter a noun:
#chandelier
#Enter a verb:
#screamed
#Enter a noun:
#pickup truck
#It would then create the following text file:

#The silly panda walked to the chandelier and then screamed. A nearby
#pickup truck was unaffected by these events.
#The program should print the results to the screen in addition to saving them to a new text file.

#if file doesn't exist, print something to screen and have user invoke program again
from pathlib import Path

def declare_user_file():
user_provided_file = input("Provide a sample text file to play around with: ")
user_provided_file_path = Path(f'./{user_provided_file}')
user_provided_file_path.exists()

if user_provided_file_path.exists() == True:
    file_rw_test_mechanism(user_provided_file_path)
else print("File does not exist. Start program and try again.")
    exit()

def file_rw_test_mechanism(user_provided_file):

file_obj = open(f'{user_provided_file_path}', encoding='utf-8')
content = file_obj.read()
file_obj.close()
file_obj = open(f'{user_provided_file_path}', 'w', encoding='utf-8')
file_obj.write('Hello, world!')
file_obj.close()



# My own fun sentence below:

# The ADJECTIVE wizard stood outside the Grand Exchange and tried to NOUN a rune scimitar for his ADJECTIVE friend. Suddenly, a NOUN appeared in Varrock and began to VERB ADVERB, causing every player nearby to VERB.

# for entirely capitalized words in a string, remap placeholder WORDS to user-provided input; don't think this would be a usecase for positional parameters necessarily. What is the Sed equivalent here but based on location of everything here?

# do we split every word out first? for word in string
# how do we decide on maximum amount of input or can this hypothetically go forever? is there some sort of buffer limit for how much can be read or can we max based on maybe idk five sentences at max. we can figure that out another time

# if VERB print Enter a verb
# if NOUN print enter a noun
# if adjective print enter an adjective
# if adverb print enter an adverb

# so a function with a single parameter which is essentially just a filepath?)

#new file should have some sort of random entropy maybe once we're done having fun i imagine'



