#
# This program count how many positive and negative input by user
#

# if user input 0, terminate get user input progress
stop = False
# store how many positive values in user input
positive = 0
# store how many negative values in user input
negative = 0

# Get user input until user input 0
while not stop:
    a = int(input("Your number: "))
    if a > 0:  # if user input is positive, update positive value
        positive = positive + 1
    elif a < 0:  # if user input is negative, update negative value
        negative = negative + 1
    else:  # if user input 0, terminate this progress
        stop = True

# Print result
print(f"Positive values: {positive}")
print(f"Negative values: {negative}")
