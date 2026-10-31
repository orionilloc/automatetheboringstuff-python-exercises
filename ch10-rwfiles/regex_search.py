# Regex Search
# Write a program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression, then prints the results to the screen.


# open the file. Need to find all files in lets just say the current folder. opens it trhgen searches line by line

# open every .txt file in there (needs to align with structure of filename rather than filetype orcontetns i guess?)

# user provides regex as a parameter provided to the function; oh how do we read regex effectively back? how much escaping might we need

#user provided regex becomes regex expression we user
# ensure that the matched line is thrown in there andn ot the just the word
# essentially doing a grep function based on the work that we have here
# then print that to the screen

# grab current dir, then iterate through all files

from pathlib import Path
import re


#grab user input
user_provided_regex = input("Provide regex to check .txt files in the current working directory: ")

# need to grab that list of all files somehow
current_working_directory = Path.cwd()
txt_files = current_working_directory.glob('*.txt')
for file in txt_files:
    print(file.name)
    pattern = re.compile(r'{user_provided_regex}')
    match = pattern.search(content)
    while match:
        match = pattern.search(content)
    return content

#iterate over all files
directory_path = Path('directory')
for file_path in directory_path.iterdir():
    print(file_path)
    return

def file_read_mechanism(indirectory_file_path):
    while
    file_obj = open(f'{indirectory_file_path}', encoding='utf-8')
    content = file_obj.read()
    file_obj.close()
    return content
