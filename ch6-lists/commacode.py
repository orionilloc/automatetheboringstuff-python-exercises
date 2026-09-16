# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.

# I neglected to make this a function. Oh well.

while True:
    print("Enter at least three items to see desired output.")
    user_list_input = input()
    user_list_input = user_list_input.split()
    if len(user_list_input) >= 3:
        user_list_input = ', ' .join(user_list_input[:-1]) + ", and " + user_list_input[-1]
        print(user_list_input)
    else:
        print("Not enough items in list. Enter at least three items to see desired output.")
