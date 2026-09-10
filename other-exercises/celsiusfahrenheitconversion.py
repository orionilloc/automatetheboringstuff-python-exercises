# celsius to fahrenheit
# fahrenheitto celsius

# number conversion

#input validation (ensuring that its F or C - then have a portion split to be the number conversion)o

# user_temperature
# temperature_scale
#then output
# need a temperature conversion function in here as well- but how much can be nested in here
#def temperature_conversion():
#    if user_temperature_scale == str('F'):
#        do some math
#    else:
#        do some math to convert from celsius to fahrenheit
# need actual math sequencing in here as well

# see below- have i essentially made a use pane and how should this be formatted here

while True:
    print("Enter a temperature and temperature scale to convert from: ")
    print("Example user input: 84 F")
    print("Example temperature conversion: 28.88888888888889 C")
    print("")
    user_input = input("Enter a temperature and temperature scale to convert from: ")
    user_temperature_number, user_temperature_scale = user_input.split()

    converted_temperature_number_to_celsius = (int(user_temperature_number) -32) * 5 / 9
    print(converted_temperature_number_to_celsius)
    converted_temperature_number_to_fahrenheit = (int(user_temperature_number) * 9 / 5 ) + 32
    print(converted_temperature_number_to_fahrenheit )
    break


#print(f' {user_temperature_number} {user_temperature_scale} converts to {converted_temperature_number} {converted_temperature_scale}. Very cool!')
#try:
#if:
    #second value is f? then convert to c
#else:
#except
#
# (0°C × 9/5) + 32 = 32°F
# include try and except somewhere in here
#
# store first field as integer - second field as F or C (cant be any other one here)
# next version would have more input validation or possibly something else more fun
