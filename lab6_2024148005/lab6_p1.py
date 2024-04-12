#
# This program takes the first name and last name entered by user, and displays the last name,
# and first letter of first name.
#

# Take user's name
name = input("Enter a first and last name: ")
# Variable that store first name
first_name = ""
# Variable that store last name
last_name = ""
# Variable that store name data
name_data = ""

# Find first and last name in user input using for loop
for letter in name:
    if letter.isalpha():  # If letter is alphabet, add letter to name_data
        name_data += letter
    elif letter.isspace() and name_data != "" and first_name == "":  # After find all firstname,
        first_name = name_data  # Assign into first_name variable
        name_data = ""  # Reset name_data variable for find last name

last_name = name_data

# Split user's name to first name and last name using split method
name_list = name.split(" ")

# Print result
print(f"{last_name}, {first_name[0]}.")
