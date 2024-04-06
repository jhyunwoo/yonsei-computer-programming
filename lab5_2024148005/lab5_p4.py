#
# This program print triangle of height n
# user input n value and use this value to create triangle
#

# Get n value from user
n = int(input("Enter an integer: "))

# Print triangle using for loop
for i in range(1, n+1):
    # Print blank
    print(" "*(i-1), end="")
    # Print *
    print("*"*(n*2-i*2+1))
