import random
number_of_streaks = 0
for experiment_number in range(10000):  # Run 100,000 experiments total.
    # Code that creates a list of 100 'heads' or 'tails' values
    coin_flip_number = 0
    heads_tails_list = list(random.choice(["H", "T"]))
    while coin_flip_number <= 100:
        heads_tails_list.append(random.choice(["H", "T"]))
        coin_flip_number += 1
    print(heads_tails_list)


    # Code that checks if there is a streak of 6 heads or tails in a row

###print('Chance of streak: %s%%' % (number_of_streaks / 100))

#ok so cant be the print function in here

#+1 to add to either sttreak value

#is random.choice being stored accidentally as a string- answer is yes
#making sense of core logic, but clearly not the actual soluton
