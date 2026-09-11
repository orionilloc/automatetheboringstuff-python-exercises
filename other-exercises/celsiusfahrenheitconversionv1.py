while True:
    print("Enter a temperature and temperature scale to convert from: ")
    print("Example user input: 84 F")
    print("Example temperature conversion: 28.88888888888889 C")
    print("")
    user_input = input("Enter a temperature and temperature scale to convert from: ")
    user_temperature_number, user_temperature_scale = user_input.split()

    if user_temperature_scale in ['F', 'f']:
        converted_temperature_number_to_celsius = (int(user_temperature_number) -32) * 5 / 9
        print(f'{converted_temperature_number_to_celsius} C')
    elif user_temperature_scale in ['C', 'c']:
        converted_temperature_number_to_fahrenheit = (int(user_temperature_number) * 9 / 5 ) + 32
        print(f'{converted_temperature_number_to_fahrenheit} F')
    break
