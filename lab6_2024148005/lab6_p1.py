#
# This program takes the first name and last name entered by user, and displays the last name,
# and first letter of first name.
#

# Take user's name
name = input("Enter a first and last name: ")

# Split user's name to first name and last name using split method
name = name.split()

# Print result
print(f"{name[1]}, {name[0][0]}.")
