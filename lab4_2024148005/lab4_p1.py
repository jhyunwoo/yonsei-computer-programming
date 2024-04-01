#
# This program get user's income and calculate tax (USD)
#

# Get income from user input and convert to int type
income = int(input("Enter the taxable income in USD: "))

# Set tax variable
tax = 0

# calculate tax using if else
if income <= 750:  # if income is lower or equal than 750
    tax = income * 0.03
elif income <= 2250:  # if income is lower or equal than 2250
    tax = 7.5 + (income-750) * 0.06
elif income <= 3750:  # if income is lower or equal than 3750
    tax = 37.5 + (income-2250) * 0.09
elif income <= 5250:  # if income is lower or equal than 5250
    tax = 82.5 + (income-3750) * 0.12
elif income <= 7000:  # if income is lower or equal than 7000
    tax = 142.5 + (income-5250) * 0.15
else:  # if income is bigger than 7000
    tax = 230.00 + (income-7000) * 0.18

# Print result
print(f"Tax due: {format(tax, '.2f')} USD")

