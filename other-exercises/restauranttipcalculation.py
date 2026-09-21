# Write a program that asks for the meal price with input(), then asks for a tip percentage the same way. Convert both to the right numeric type, calculate the tip amount and the total, then print both using string concatenation

initial_meal_spend = float(input("How many dollars did your meal cost? "))
meal_tip_percentage = float(input("What percentage will you tip? "))
meal_tip_calculation = initial_meal_spend * (meal_tip_percentage / 100)
total_meal_spend = initial_meal_spend + meal_tip_calculation
print("Your meal cost $" + str(initial_meal_spend) + ", with a tipped percentage of " + str(meal_tip_percentage) + "%. Your total meal cost will be: $" + str(total_meal_spend))
