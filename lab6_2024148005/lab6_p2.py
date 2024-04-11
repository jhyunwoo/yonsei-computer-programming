#
# This program takes fraction and find the lowest terms of fraction
#

# Take fraction from user input and convert string to list
fraction = list(input("Enter a fraction: "))

# Variable that store numerator
numerator = None
# Variable that store denominator
denominator = None

# Variable that store numerator or denominator
num = ""

# Find numerator and denominator in fraction list
for char in fraction:
    if char == "/":  # if char is equal to '/', assign num variable to numerator and init num variable
        numerator = int(num)
        num = ""
    elif char.isnumeric():  # if char is numeric, add char in num variable
        num = num + char

# Assign num into denominator
denominator = int(num)

# Variable that store numerator. It will be used in euclid algorithm.
a = numerator
# Variable that store denominator. It will be used in euclid algorithm.
b = denominator
# Variable that store gcd
gcd = None

# Use Euclid Algorithm to find GCD
c = a % b

if c != 0:  # if c is not 0, b assign to a, c assign to b
    a = b
    b = c
else:  # else, GCD is b
    gcd = b

# Find GCD when c is not 0
while c != 0:
    c = a % b
    if c != 0:  # if c is not 0, b assign to a, c assign to b
        a = b
        b = c
    else:  # else, GCD is b
        gcd = b

# If denominator of lowest terms is 1, skip print denominator
if denominator / gcd == 1:
    print(f"In lowest terms: {int(numerator/gcd)}")
else:  # else, print whole lowest terms
    print(f"In lowest terms: {int(numerator/gcd)}/{int(denominator/gcd)}")
