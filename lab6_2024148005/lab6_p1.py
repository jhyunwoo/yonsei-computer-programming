#
# This program takes the first name and last name entered by user, and displays the last name,
# and first letter of first name.
#

# Take user's name
name = input("Enter a first and last name: ")

# Variable that store index of first letter in user input
index_of_first_letter = 0

# Find first letter index using for loop
for cha in name:
    if cha == " ":  # if cha is space, increase index_of_first_letter variable
        index_of_first_letter += 1
    else:  # if cha is letter, stop find index_of_first_letter
        break

name = name[index_of_first_letter:]

# Split user's name to first name and last name using split method
name_list = name.split(" ")

# Print result
print(f"{name_list[1]}, {name_list[0][0]}.")
