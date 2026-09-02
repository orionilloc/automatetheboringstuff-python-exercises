def collatz(number):
    if int(number) % 2 == 0: # if even
        result = int(number) // 2
    else: # if odd
        result = int(number) * 3 + 1
    print(result, end=' ')
    return result

number = input('Please enter a number:')

while number != 1:
    number = collatz(number)
