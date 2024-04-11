#
# This program takes words from user input and store word that words whose first letter occurs again within the word
# and print the list.
#

# List that store words
words = []

# Boolean that control while loop
stop = False

# Take user input until user input q
while not stop:
    word = input("Enter a word (q to quit): ")  # Take user input
    if word == "q":  # if user input q, stop the while loop
        stop = True
    else:  # check the user input
        lowercase_word = word.lower()
        first_letter = lowercase_word[0]
        if first_letter in lowercase_word[1:]:  # if the word whose first letter occurs again within the word, append it to words list
            words.append(word)

# Sort words list
words.sort()

# Print result
print(words)
