"""
Name: Hyunwoo Jeon
Student ID: 2024148005
Lab problem: lab13_p7.py
"""

#
# This program contains searchDir function
# that find all txt files in dir and sub dir
#

import os


def searchDir(directory, s):
    """
    Recursively searches 'directory' for
    .txt files that contain string s.

    :param directory The path to the directory to search.
    :param s The string to search for within the .txt files.

    :return A list of file paths of .txt files
    that contain the string `s`.
    """
    # List to store the paths of .txt files that contain the string `s`
    included = []
    # Get a list of all files and directories in the given directory
    list_of_files = os.listdir(directory)

    for f in list_of_files:
        # Flag to check if the current file contains the string `s`
        is_included = False
        # Get the full path of the current file or directory
        full_path = os.path.join(directory, f)

        # If the current path is a directory, recursively search it
        if os.path.isdir(full_path):
            included += searchDir(full_path, s)
        # Check if the current file is a .txt file
        elif f.endswith(".txt"):
            # Open the .txt file for reading
            with open(full_path, 'r') as open_txt:
                for line in open_txt:  # Read through each line in the file
                    if s in line:  # If the string `s` is found in the line
                        is_included = True  # Set the flag to True
                        break  # Exit the loop since we found the string `s`

        if is_included:  # If the .txt file contains the string `s`
            # Add the file path to the included list
            included.append(full_path)

    # Return the list of .txt files that contain s
    return included

