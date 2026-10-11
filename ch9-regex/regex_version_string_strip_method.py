# Write a function that takes a string and does the same thing as the strip() string method. If no other arguments are passed other than the string to strip, then the function should remove whitespace characters from the beginning and end of the string. Otherwise, the function should remove the characters specified in the second argument to the function.

#remove whitespace beginning of a string
#remove whitespace end of a string
#second argument to function removes characters specified
#can i do re_compile with a user-provided var of some sort

import re

provided_string = input("Provide a string to check against: ")
characters_to_remove = input("Provide some characters to remove: ")

def regex_version_string_strip_method(text, characters=None):
    if characters is None:
        strip_regex = re.compile(r'^\s+|\s+$')
    else:
        re.escape(characters)
        strip_regex = re.compile(rf"^[{characters}]+|[{characters}]+$")
    return strip_regex.sub('', text)

print(regex_version_string_strip_method(provided_string, characters_to_remove or None))

