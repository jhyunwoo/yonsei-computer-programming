#
# This program calculate math expression using reverse polish notation.
#

# Import stack and sys modules
import stack
import sys

# Keep continue until user input not an operator and not an operand
while True:
    error = False  # If error occurs, print out error comment
    # Get expression from user input
    expression = input("Enter an RPN expression: ")
    # Convert string to list
    rpn = expression.split()

    operator = 0
    operand = 0
    # Check if expression contains not an operator and not an operand
    for char in rpn:
        if char.isnumeric():
            operand += 1
        elif char == "+" or char == "-" or char == "*" or char == "/" or char == "=":
            operator += 1
        else:
            sys.exit()

    if operand != operator:
        error = True

    # If last object of list is not "=", handle as error
    if rpn[-1] != "=":
        error = True
    else:  # Else, pop "=" from list
        stack.pop(rpn)

    count = 0  # Variable that store where the target of the list
    while len(rpn) > 1 and not error:  # Continue until rpn length is bigger than 1 and does not occur error
        if rpn[count] == "*":  # Calculate multiply
            result = float(rpn[count - 2]) * float(rpn[count - 1])
            rpn = rpn[:count - 2] + [result] + rpn[count + 1:]
            count -= 1
        elif rpn[count] == "/":  # Calculate divide
            if float(rpn[count-1]) == 0:
                error = True
            else:
                result = float(rpn[count - 2]) / float(rpn[count - 1])
                rpn = rpn[:count - 2] + [result] + rpn[count + 1:]
                count -= 1
        elif rpn[count] == "+":  # Calculate plus
            result = float(rpn[count - 2]) + float(rpn[count - 1])
            rpn = rpn[:count - 2] + [result] + rpn[count + 1:]
            count -= 1
        elif rpn[count] == "-":  # Calculate minus
            result = float(rpn[count - 2]) - float(rpn[count - 1])
            rpn = rpn[:count - 2] + [result] + rpn[count + 1:]
            count -= 1
        # If rpn[count] is not operator, increase count variable
        elif (str(rpn[count])).isnumeric() and rpn[count] != "=":
            count += 1
        else:  # If rpn[count] is not an operator or not an operand, handle as error
            error = True

    # Print out result
    if not error:
        if float.is_integer(rpn[0]):
            print(f"Value of expression: {int(rpn[0])}")
        else:
            print(f"Value of expression: {format(rpn[0], '.2f')}")
    else:
        print("Evaluation error")
