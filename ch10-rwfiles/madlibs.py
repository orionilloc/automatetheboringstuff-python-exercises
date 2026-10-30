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

from pathlib import Path
import re
import datetime

def retrieve_present_time():
        now = datetime.datetime.now()
        string_timestamp = now.strftime("%Y_%m_%d_%H_%M_%S")
        return string_timestamp

def declare_user_file():
    user_provided_file = input("Provide a sample text file to play around with: ")
    user_provided_file_path = Path(f'./{user_provided_file}')
    string_timestamp = retrieve_present_time()
    output_path = Path(f'./{user_provided_file}_modified_{string_timestamp}')

    if user_provided_file_path.exists() == True:
        return user_provided_file_path, output_path
    else:
        print("File does not exist. Start this program and try again.")
        exit()

def file_read_mechanism(user_provided_file_path):
    file_obj = open(f'{user_provided_file_path}', encoding='utf-8')
    content = file_obj.read()
    file_obj.close()
    return content

def silly_word_replacement(content):
    pattern = re.compile(r'\b(ADJECTIVE|NOUN|VERB|ADVERB)\b')
    match = pattern.search(content)
    while match:
        silly_word = input(f"Enter a {match.group().lower()}: ")
        content = pattern.sub(silly_word, content, count=1)
        match = pattern.search(content)
    return content

def file_write_mechanism(output_path, content):
    file_obj = open(f'{output_path}', 'x', encoding='utf-8')
    file_obj.write(f'{content}')
    file_obj.close()

user_provided_file_path, output_path = declare_user_file()
content = file_read_mechanism(user_provided_file_path)
content = silly_word_replacement(content)
print(content)
file_write_mechanism(output_path, content)
