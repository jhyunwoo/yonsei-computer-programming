#
# This program check user parentheses is nested or not nested using stack module
#

# Import stack module
import stack

# Get user input
parentheses = input("Enter parentheses and/or braces: ")

# Delete braces if same type of braces is next to each other
for i in range(0, len(parentheses)//2):
    for j in range(0, len(parentheses) - 1):  # For loop for check all character ins parentheses value
        if (parentheses[j] == "(" and parentheses[j+1] == ")") or (parentheses[j] == "{" and parentheses[j+1] == "}")\
                or (parentheses[j] == "[" and parentheses[j+1] == "]"):  # If same type of braces is next to each other
            parentheses = parentheses[:j] + parentheses[j+2:]  # Slice the braces
            break

# Print Result
if stack.isEmpty(list(parentheses)):  # Check user input is nested using stack module isEmpty function
    print("Nested properly.")
else:
    print("Not properly nested.")
