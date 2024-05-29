#
# This module provide 3 function that parse string.
#

# Welcome Text
print("This module is a parser.")
print("It is designed to parse any input text.")


def letterNum(inputString):
    """
    Count all letter characters in string ``inputString'' and append the
    result to file ``answer.txt''.
    The number of letter characters must be written to the file:
    letterNum('abA1 23') -> writes 3
    letterNum('!') -> writes 0
    """
    counter = 0  # Initialize counter to count letter characters
    for letter in inputString:
        if letter.isalpha():  # Check if the character is a letter
            counter += 1  # Increment counter if it is a letter
    # Open the file "answer.txt" in append mode
    answer_file = open("answer.txt", "a")
    # Write the count of letter characters followed by a newline
    answer_file.write(str(counter) + "\n")
    # Close the file to save changes
    answer_file.close()


def wordLong(inputString):
    """
    Find and return the last longest word in string ``inputString'' and
    append the result to file ``answer.txt''. If the string is empty,
    nothing is written.
    The last longest word in the string must be written to the file:
    wordLong(‘abc defg hijk’) -> writes hijk
    wordLong(‘!’) -> writes !
    """
    # Split the input string into a list of words
    list_of_words = inputString.split()
    longest_word = ''  # Initialize variable to hold the longest word
    for word in list_of_words:  # For Loop for check all word in list_of_words
        if len(word) >= len(longest_word):  # Check if the current word is longer than the longest_word
            longest_word = word  # Update longest_word if the current word is longer
    if longest_word != '':  # Only write to the file if longest_word is not empty
        # Open the file "answer.txt" in append mode
        answer_file = open("answer.txt", "a")
        # Write the longest word followed by a newline
        answer_file.write(longest_word + "\n")
        # Close the file to save changes
        answer_file.close()


def vowelNum(inputString):
    """
    Count the number of vowels in string ``inputString'‘ and append the
    result to file ``answer.txt''. Y is not considered a vowel.
    The number of vowels must be written to the file:
    vowelNum(‘fox WOLF cat DOG’) -> writes 4
    vowelNum(‘fly shyly’) -> writes 0
    """
    counter = 0  # Initialize counter to count vowel characters
    for letter in inputString:  # For loop for check all letter in inputString
        lower_letter = letter.lower()  # Convert the character to lowercase
        if lower_letter in "aeiou":  # Check if the character is a vowel
            counter += 1  # Increment counter if it is a vowel
    # Open the file "answer.txt" in append mode
    answer_file = open("answer.txt", "a")
    # Write the count of vowels followed by a newline
    answer_file.write(str(counter) + "\n")
    # Close the file to save changes
    answer_file.close()
