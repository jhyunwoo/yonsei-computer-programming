# Sparse Text Program

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def createModifiedFile(input_file, output_file):
    """
    For text file input_file, creates a new version in file output_file
    in which all instances of vowels are removed.
    """
    # Initialize empty_str, num_total_chars, num_removals
    empty_str = ''  # Empty string for replace vowels
    num_total_chars = 0  # Count total chars in input file
    num_removals = 0  # Count removed chars

    # Iterate over each line in the input file
    for line in input_file:
        # Save original line length
        orig_line_length = len(line.strip('\n'))
        num_total_chars += orig_line_length

        # Remove all occurrences of vowels
        modified_line = line
        # Check all vowels and replace it to empty string
        for char in vowels:
            modified_line = modified_line.replace(char, empty_str)

        # Calculate number of removed characters
        num_removals += orig_line_length - len(modified_line.strip('\n'))

        # Output line to screen and output file
        print(modified_line.strip('\n'))
        output_file.write(modified_line)

    return num_total_chars, num_removals


# --- main

# Get file name in user input
file_name = input('Enter file name (including file extension): ')
# Read file with reading mode
input_file = open(file_name, 'r')
# Create new file name that contain modified content
new_file_name = 'e_' + file_name
# Open new file with writing mode
output_file = open(new_file_name, 'w')

print()
# Modify input file and append data on output file, get num_total_chars and num_removals data
num_total_chars, num_removals = createModifiedFile(input_file, output_file)

# Close the input and output files
input_file.close()
output_file.close()

# Display the result
print()
# Print how many vowels was removed
print(num_removals, "vowels removed")
# Print how many characters are removed and how many chars in original data
print(num_removals, "out of", num_total_chars, "characters removed")
# Print percentage of data lost
print('Percentage of data lost:', int((num_removals / num_total_chars) * 100), '%')
# Print Modified text file
print('Modified text in file', new_file_name)
