#
# This program convert US dollars to Korean won
# Exchange Rate: 1200 won = 1 dollar
#

# Print banner with symbols
print("""Currency Exchange Service
\u00A9 2024 Yonsei University
\U0001F60A All rights reserved \U0001F60A""")

# Variable that control while loop
stop = False
# Variable that store dollars
dollars = 0

while not stop:
    # Get user input and convert to float
    a = float(input("Enter amount in dollars ($): "))
    if a == 0:  # If user input is 0, stop while loop
        stop = True
    else:  # Else, add to dollars variable
        dollars += a

# Print result
print(f"Amount in Korean won (\u20A9): {format(dollars * 1200, ',.2f')}")
