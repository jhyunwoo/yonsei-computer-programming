#
# This program take fruit type and weight from user and display it.
#

from operator import itemgetter

# Variable that control while loop
stop = False

# List that store fruit type and weight
fruits = []

# Take user input until user input is q
while not stop:
    fruit_type = input("Enter a fruit type (q to quit): ")  # Take user input

    if fruit_type == "q":  # if input is q, stop the while loop
        stop = True
    else:
        weight = int(input("Enter the weight in kg: "))  # Take fruit's weight

        # List that store all fruit types in fruits list
        fruits_types = []
        # Create fruits_types list using for loop
        for fruit in fruits:
            fruits_types.append(fruit[0])  # append all fruit type into the fruits_types list

        if fruit_type in fruits_types:  # if fruits has already same type of fruit, just add weight into previous fruit weight
            fruits[fruits_types.index(fruit_type)][1] = fruits[fruits_types.index(fruit_type)][1] + weight
        else:  # else, create new fruit info
            fruits.append([fruit_type, weight])

# Sort fruits list order by fruit type
fruits.sort(key=itemgetter(0))

# If fruits length is bigger than 0, print result
if len(fruits) > 0:
    for fruit in fruits:
        print(f"{fruit[0]}, {fruit[1]}kg.")
else:  # Print it when fruits list contains nothing
    print("No data received, exiting.")
