#
# This program get all names from user and count how many a letters in names
#

# List that store name
names = []
# Variable that control while loop
stop = False

while not stop:
    # Get user input
    name = input("Enter a name (q to quit): ")
    if name == "q" or name == "quit":  # If user input q or quit, stop while loop
        stop = True
    else:  # Else, append user input to the names list
        names.append(name.lower())

# Variable that store how many a letter in the names
count = 0

# Count all a letters in the names
for n in names:
    count += n.count("a")

# Print result
print(f"Appearance of letter 'a': {count}")
