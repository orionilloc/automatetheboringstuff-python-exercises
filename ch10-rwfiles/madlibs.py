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

import re
from pathlib import Path

def declare_user_file():
    user_provided_file = input("Provide a sample text file to play around with: ")
    user_provided_file_path = Path(f'./{user_provided_file}')

    if user_provided_file_path.exists() == True:
        return user_provided_file_path
    else:
        print("File does not exist. Start this program and try again.")
        exit()

def file_rw_test_mechanism(user_provided_file_path):
    file_obj = open(f'{user_provided_file_path}', encoding='utf-8')
    content = file_obj.read()
    file_obj.close()
   # file_obj = open(f'{user_provided_file_path}', 'x', encoding='utf-8')
   # file_obj.write('Hello, world!')
   # file_obj.close()
    return content

user_provided_file_path = declare_user_file()
file_rw_test_mechanism(user_provided_file_path)


# for list of words in content print this
#however i declare replacement silly word
# oh does this become a list; hm maybe
# but issue now is that i only get a single letter of output here rather than the entire word to be entered; need to catch
#the entire word
madlibs_parts_of_speech = ['ADJECTIVE', 'NOUN', 'VERB', 'ADVERB']

#oh wait maybe i should look into regex
for madlibs_parts_of_speech in content:
    replacement_silly_word = input(f"Enter a {madlibs_parts_of_speech}: ")
    #grab word to replace then that becomes the new text
    # i literally just want a sed function. why cant bash just have better data structures
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



