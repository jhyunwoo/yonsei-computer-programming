#
# This program encrypts or decrypts a file using a random key.
#

from random import random

# List of characters to be used for encryption and decryption
characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
              "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
              "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d",
              "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
              "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
              "y", "z", "0", "1", "2", "3", "4", "5", "6", "7",
              "8", "9", " ", "."]

# Copy of the list of characters for key generation
key_characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                  "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d",
                  "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                  "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                  "y", "z", "0", "1", "2", "3", "4", "5", "6", "7",
                  "8", "9", " ", "."]

# Prompt the user for the filename
file = input("Enter a filename: ")
# Extract the base filename
filename = file.split(".")[0]
# Extract the base extension
file_extension = file.split(".")[-1]

# If file is txt file
if file_extension == "txt":
    # Encrypt the file if the extension is .txt
    key = {}  # Dictionary to store the encryption key
    counter = 0  # Variable that count generate random key
    # Generate the encryption key by mapping each character to a random character from key_characters
    while len(key_characters) > 0:
        key[characters[counter]] = key_characters.pop(int(random() * len(key_characters)))
        counter += 1
    key["="] = "="  # Special character mapping for "="
    key["\n"] = "\n"  # Special character mapping for newline

    try:
        # Open the original file for reading
        original_file = open(file, "r")
    except FileNotFoundError:
        raise FileNotFoundError("Cannot open the file")

    # Open the output file for the encrypted message
    enc_file = open(filename + ".enc", 'w')
    # Read each line from the original file and write the encrypted characters to the new file
    for line in original_file:
        for char in line:  # For loop for check all char in line
            enc_file.write(key[char])  # Write encrypted char in file
    original_file.close()  # Close original file
    enc_file.close()  # Close encrypted file

    # Save the encryption key to a .key file
    key_file = open(filename + ".key", 'w')
    for char in characters:  # Check all char in characters for generate key file
        key_file.write(f"{char},{key[char]}\n")  # Write key on the file
    key_file.write("=,=")  # Special character mapping for "="
    key_file.close()  # Close key file
elif file_extension == "enc":  # Decrypt encrypted file if file extension is .enc
    try:
        # Open the key file for reading
        key_file = open(filename + ".key", 'r')
    except FileNotFoundError:
        raise FileNotFoundError("Cannot open the key file")

    key = {}  # Dictionary to store the decryption key
    # Read the key file and create a key dictionary for decryption
    for line in key_file:
        key[line.split(",")[1][0]] = line.split(",")[0]
    key_file.close()  # Close key file

    # Open the encrypted file and the output file for the decrypted message
    enc_file = open(filename + ".enc", 'r')
    dec_file = open(filename + ".txt", 'w')
    # Read each line from the encrypted file and write the decrypted characters to the new file
    for line in enc_file:
        for char in line:  # For loop for check all char in line
            if char != "\n":  # If char is not enter sign
                dec_file.write(key[char])  # Write decrypted char on file
            else:  # if char is enter sign
                dec_file.write("\n")  # Write enter sign on file
    enc_file.close()  # Close encrypted file
    dec_file.close()  # Close decrypted file
