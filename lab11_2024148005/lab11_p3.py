"""
File WordCount.py

Program to count the number of occurrences of a word
in a textfile.
"""

def getFile():
    """
    Returns the file name and associated file object for reading the
    file as a tuple of the form (file_name, input_file).
    """
    input_file_opened = False  # Flag to check if the file is successfully opened
    while not input_file_opened:
        try:
            # Prompt the user to enter the input file name with extension
            file_name = input('Enter input file name (with extension): ')
            # Attempt to open the file in read mode
            input_file = open(file_name, 'r')
            input_file_opened = True  # Set flag to True if file opens successfully
        except OSError:
            # Print error message if file opening fails and prompt user again
            print('Unable to open input file, please reenter')
    return (file_name, input_file)  # Return the file name and file object

def countWords(input_file):
    """
    Returns the number of occurrences
    of each word in the provided input_file object.
    """
    # Define word delimiters for splitting lines into words
    word_delimiters = (' ', ',', ';', ':', '.','\n', '"', "'", '(', ')')

    file_words = []  # List to store all words from the file
    count_word = []  # List to store tuples of word and its count
    word_list = []  # List to store unique words

    # Iterate over each line in the file
    for line in input_file:
        line = line.lower()  # Convert line to lower case
        # Replace each delimiter in the line with a space
        for delimiter in word_delimiters:
            line = line.replace(delimiter, ' ')
        # Split the line into words and append to file_words if alphabetic
        for word in line.split():
            if word.isalpha():
                file_words.append(word)

    file_words.sort()  # Sort the list of words alphabetically
    # Create a list of unique words
    for word in file_words:
        if word not in word_list:
            word_list.append(word)

    # Count occurrences of each unique word and append to count_word list
    for word in word_list:
        count_word.append((word, file_words.count(word)))

    return count_word  # Return the list of tuples containing word counts

# Get the file name and input file object from the user
file_name, input_file = getFile()

# Count the words in the input file
counted_word_list = countWords(input_file)

# Open an output file to write the word counts, with the same name as input but with .wc extension
output_file = open(file_name.split(".")[0] + ".wc", 'w')

# Write the word counts to the output file
for counted in counted_word_list:
    output_file.write(str(counted[0]) + ": " + str(counted[1]) + "\n")
