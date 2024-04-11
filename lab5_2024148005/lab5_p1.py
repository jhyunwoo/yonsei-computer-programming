#
# This program store all user input bigger than 0 and print out second-largest number
# when user input 0 or negative number.
#

# while loop stop variable
stop = False

# Store largest number
first = 0
# Store second-largest number
second = 0

# while loop
while not stop:
    # Get user input and convert to float type
    a = float(input("Enter a number: "))
    if a > 0:  # if user input is bigger than 0
        if a > first:  # if user input is bigger than first number, user input is assigned to first variable
            second = first  # Fucking mistake!!
            first = a
        elif a > second:  # if user input is bigger than second number, user input is assigned to second variable
            second = a
    else:  # else, stop the while loop
        stop = True

# Print result
print(f"The second largest number entered was {format(second, '.2f')}")
