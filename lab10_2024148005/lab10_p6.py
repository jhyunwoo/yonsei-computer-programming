# Sparse Text Program

def createModifiedFile(input_file, output_file):
    """
    For text file input_file, creates a new version in file output_file
    in which all instances of the letter 'e' are removed.
    """
    # Initialize variable that count total chars and count removed chars
    num_total_chars = 0
    num_removals = 0

    # For loop for check all lines in input_file
    for line in input_file:
        # if input_file is ends with '\n'
        if line[-1] == '\n':
            orig_line_length = len(line) - 1  # Set orig_line_length with -1
        else:  # if the line does not contain '\n'
            orig_line_length = len(line)  # Set orig_line_length
        num_total_chars += orig_line_length  # Add orig_line_length to num_total_chars

        # Initialize modified_line that contains modified data
        modified_line = ""
        # Variable that count whitespace
        whitespace = 0
        # For loop for check all chars in line
        for char in line:
            if char == " ":  # If char is whitespace, increment whitespace variable
                whitespace += 1
            else:  # If char is not whitespace, initialize whitespace variable
                whitespace = 0
            if whitespace < 2:  # add char in modified_line variable when char is not extra whitespace
                modified_line += char

        if line[-1] == '\n':  # If line is ends with '\n', add length of removed in num_removals with -1
            num_removals += (orig_line_length - (len(modified_line) - 1))
        else:  # If line is not ends with '\n', add length of removed in num_removals
            num_removals += (orig_line_length - len(modified_line))

        # Print out modified line
        print(modified_line.strip('\n'))
        # Write modified line data on file
        output_file.write(modified_line)

    return num_total_chars, num_removals


# --- main

# open files for reading and writing
file_name = input('Enter file name (including file extension): ')
input_file = open(file_name, 'r')
new_file_name = 'r_' + file_name
output_file = open(new_file_name, 'w')

# create file with all letter e removed
print()
num_total_chars, num_removals = createModifiedFile(input_file, output_file)

# close current input and output files
input_file.close()
output_file.close()

# Display the result
print()
# Print how much whitespace was removed
print(num_removals, "whitespace characters removed")
# Print how many characters are removed and how many chars in original data
print(num_removals, "out of", num_total_chars, "characters removed")
# Print percentage of data lost
print('Percentage of data lost:', int((num_removals / num_total_chars) * 100), '%')
# Print Modified text file
print('Modified text in file', new_file_name)
