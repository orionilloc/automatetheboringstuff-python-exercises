# Write a program that asks for a permission digit (0-7) with input(), then uses if/elif/else and the or operator to check whether that digit grants write access to everyone -- true for 2, 3, 6, and 7 -- and prints the result


try:
    permission_digit = int(input("Please provide a permission digit: "))
    if permission_digit in [2, 3, 6, 7]:
        print("Provided permissions digit grants write access to everyone; consider using a more granular permission set.")
    elif permission_digit in [0, 1, 4, 5]:
        print("Provided permissions digit doesn't grant write access to everyone; looks good to me!")
    else:
        print("Invalid number provided")
except ValueError:
    print("Invalid permissions digit provided.")
