import random
number_of_streaks = 0
streak_H = ["H"] * 6
streak_T = ["T"] * 6

for experiment_number in range(10000):  # Run 100,000 experiments total.

    # Code that creates a list of 100 'heads' or 'tails' values
    coin_flip_number = 0
    heads_tails_list = []
    while coin_flip_number < 100:
        heads_tails_list.append(random.choice(["H", "T"]))
        coin_flip_number += 1

    # Code that checks if there is a streak of 6 heads or tails in a row
    if any(heads_tails_list[i:i+6] == streak_H or heads_tails_list[i:i+6] == streak_T for i in range(len(heads_tails_list) - 5)):
        number_of_streaks += 1
print('Chance of streak: %s%%' % (number_of_streaks / 100))
