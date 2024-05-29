#
# This program count all letters in line and return counted list
#

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']

def countAllLetters(line):
    """
    Counts letters in 'line' and returns result list. If the line
    does not contain any letter, returns an empty list.
    Note 1: the list of letters must be sorted alphabetically.
    (This is a requirement in addition to the textbook problem.)
    Note 2: your letters in the result-list must be stored in lower-case.
    """
    # Initialize a counter list with zeros, one for each letter in the letters list
    counter = [0] * len(letters)

    # Iterate over each character in the input line
    for letter in line:
        # Check if the character is a letter
        if letter.isalpha():
            # Convert the character to lower case and find its index in the 'letters' list
            index = letters.index(letter.lower())
            # Increment the counter for this letter
            counter[index] += 1

    # Initialize an empty list to store the result
    answer = []
    # Iterate over the counter list
    for i in range(len(counter)):
        # If the counter for a particular letter is not zero
        if counter[i] != 0:
            # Append a tuple (letter, count) to the result list
            answer.append((letters[i], counter[i]))

    # Return the result list
    return answer
