#
# This program get all user input and if user input is bigger than 0, store 'over' else store user input
#

# Variable that stop while loop
stop = False
# List that store user input
integers = []

# Get user input until user input is 0
while not stop:
    # Get user input and convert to int type
    a = int(input("Enter an integer: "))
    # If user input is 0, stop while loop
    if a == 0:
        stop = True
    elif a > 100:  # If user input is greater than 100, append 'over'
        integers.append("over")
    else:
        integers.append(a)

# Print result
print(integers)
