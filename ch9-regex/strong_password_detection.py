# Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong password has several rules: it must be at least eight characters long, contain both uppercase and lowercase characters, and have at least one digit. Hint: It’s easier to test the string against multiple regex patterns than to try to come up with a single regex that can validate all the rules.

import re
import getpass

def strong_password_detection():
    password_length_regex = re.compile(r'.{8,}')
    password_lowercase_regex = re.compile(r'[a-z]')
    password_uppercase_regex = re.compile(r'[A-Z]')
    password_digit_regex = re.compile(r'[0-9]')
    password_special_character_regex =  re.compile(r'\W+')

    print("Please provide a user-generated password to assess:")
    user_password = getpass.getpass()

    password_complexity_checks = [
        (password_length_regex, "at least 8 characters"),
        (password_lowercase_regex, "a lowercase letter"),
        (password_uppercase_regex, "an uppercase letter"),
        (password_digit_regex, "a number of some sort"),
        (password_special_character_regex, "a special character of some sort")
        ]

    missing_password_checks = []
    for regex, message in password_complexity_checks:
        if not regex.search(user_password):
            missing_password_checks.append(message)

    if missing_password_checks:
        print("Password is weak and missing " + ", ".join(missing_password_checks))
    else:
        print("Password is strong enough for the exercise.")

strong_password_detection()
