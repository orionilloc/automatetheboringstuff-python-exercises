def collatz(number):
    if int(number) % 2 == 0: # if even
        result = int(number) // 2
    else: # if odd
        result = int(number) * 3 + 1
    print(result, end=' ')
    return result

number = input('Please enter a non-zero number:')

while True:
    try:
        number = int(number)
        if number == 0:
            print('Invalid input provided.')
            number = input('Please enter a non-zero number:')
        else:
            break
    except ValueError:
        print('Invalid input provided.')
        number = input('Please enter a non-zero number:')

while int(number) != 1:
    number = collatz(number)
