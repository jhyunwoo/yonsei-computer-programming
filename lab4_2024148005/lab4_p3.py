#
# This program print how many digits on user input
#

# Get user input and convert into int type
a = int(input("Enter a number: "))
# Flatten the input data into positive number
b = abs(a)

# store how many digits on user input
digits = 1

# while stopping variable
stop = False

# add digits until b // 10 is not bigger than 10
while not stop:
    if b // 10 > 0:
        b = b//10
        digits = digits + 1  # add digits
    else:
        stop = True  # Stop while

# Print result
if digits == 1:  # if digit is 1
    print(f"The number {a} contains 1 digit")
else:  # if digit is bigger than 1
    print(f"The number {a} contains {digits} digits")