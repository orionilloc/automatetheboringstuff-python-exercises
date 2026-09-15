# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.


#take list value as argument- return string from there
#ok so fundamentally i needt o pull values from a list no matter what, so there is some sort of reformatting in here so we're outputting the raw list once again; is this a separate print functrion

# then i need to define the parameter in here- maybe do concatenation
spam = ['apples', 'bananas', 'tofu', 'cats']
spam = ', ' .join(spam[:-1]) + ", and " + spam[-1]
print(spam)
#def return_comma_space_returned string():

user_list_input = input() #make a list out of any of the valujes pasted essentially, using white space, maybe do as separate else
user_list_input = user_list_input.split()
user_list_input = ', ' .join(user_list_input[:-1]) + ", and " + user_list_input[-1]
print(user_list_input)
#try
# no input or invalid input detected; running default list demonstration

# part of me almost wants to avoid list format or notation and create additional hleper function to make a list out of tokens or strings based on whitespace- how does that sound
#else ValueError
print("Empty list passed as an argument to the function")


#if user fails to submit input again we can load a random dictionary of words from a python module maybe
# how can we load data and then validate that it is a list- otherwise can we make into a list from there and do some magic to create our own list


#if empty output do something else
