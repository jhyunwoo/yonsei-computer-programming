#
# Palindrome Checker Program
# without stack
#

# Welcome Text
print("This program can determine if a given string is a palindrome\n")
print("(Enter return to exit)")

# Get chars from user input
chars = input("Enter string to check: ")

# Stop while loop until user input is enter
while chars != "":
    if len(chars) == 1:  # if chars is just one character
        print("A one letter word is by definition a palindrome\n")
    else:  # Else check all character in user input
        if_palindrome = True
        for char in chars:  # Check all value
            if char.lower() != chars[len(chars) - chars.index(char) - 1].lower():  # If char is not satisfy palindrome,
                if_palindrome = False
        # Print result
        if if_palindrome:
            print(chars, "is a palindrome\n")
        else:
            print(chars, "is NOT a palindrome\n")

    # Get chars from user input
    chars = input("Enter string to check: ")