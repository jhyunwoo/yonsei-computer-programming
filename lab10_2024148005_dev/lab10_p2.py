#
# This program input 3 files name. Copy first and second files and write on third file.
#

def copyFiles(f1, f2, f3):
    """
    Copies f1 and f2 onto f3.
    The function assumes that files f1 and f2 can be opened, and that
    no error occurs in writing file f3.
    Therefore, the function will always return 0.
    (Error handling with file I/O will be part of next week's lecture.)
    """
    data = ""  # Initialize an empty string to store the combined contents of f1 and f2

    # Open file f1 in read mode
    file1 = open(f1, 'r')
    # Read the first line from file f1
    line = file1.readline()
    # Continue reading until the end of the file
    while line != '':
        data += line  # Append the line to the data string
        line = file1.readline()  # Read the next line
    file1.close()  # Close file f1 after reading all its content

    # Open file f2 in read mode
    file2 = open(f2, 'r')
    # Read the first line from file f2
    line = file2.readline()
    # Continue reading until the end of the file
    while line != '':
        data += line  # Append the line to the data string
        line = file2.readline()  # Read the next line
    file2.close()  # Close file f2 after reading all its content

    # Open file f3 in write mode
    file3 = open(f3, 'w')
    # Write the combined data from f1 and f2 into file f3
    file3.write(data)
    # Close file f3 after writing all the data
    file3.close()

    return 0  # The function always returns 0 as specified
