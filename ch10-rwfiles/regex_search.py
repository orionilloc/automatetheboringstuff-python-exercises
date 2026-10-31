# Regex Search
# Write a program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression, then prints the results to the screen.

from pathlib import Path
import re

user_provided_regex = input("Provide regex to check .txt files in the current working directory: ")

current_working_directory = Path.cwd()
txt_files = current_working_directory.glob('*.txt')
pattern = re.compile(user_provided_regex)
print("")
for file in txt_files:
    with file.open(encoding='utf-8') as file_obj:
        for line in file_obj:
            if pattern.search(line):
                print(file.name)
                print(line, end='')
                print("")
