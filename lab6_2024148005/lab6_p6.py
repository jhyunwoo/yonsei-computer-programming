#
# This program calculate exponential, cosine, and sine
#

import math

# Calculate equations until user input 0
while True:
    # Take equation from user input
    equation = input("Evaluate the equation: ")
    # if equation is 0, stop the while loop
    if equation == '0':
        break

    # Split equation input for find equation type, x, and L value
    split_equation = equation.split(" ")

    # Get equation type from split_equation
    equation_type = split_equation[0]
    # Get x value from split_equation
    x = float(split_equation[1])
    # Get L value from split_equation
    L = int(split_equation[2])

    # Variable that store equation result
    result = 0

    # Calculate expansion
    if equation_type == "exp":
        for n in range(L):
            result += (x ** n) / (math.factorial(n))
    elif equation_type == "cos":  # Calculate cosine
        for n in range(L):
            result += (((-1) ** n) / math.factorial(2*n)) * (x ** (2*n))
    elif equation_type == "sin":  # Calculate sine
        for n in range(L):
            result += (((-1) ** n) / (math.factorial(2 * n + 1))) * (x ** (2*n+1))

    # Print calculated result
    print(f"Using {L} term(s), {equation_type}({format(x, '.4f')}) is {format(result, '.6f')}")
