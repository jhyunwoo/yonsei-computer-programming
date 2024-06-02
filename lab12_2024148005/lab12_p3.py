"""
Name: Hyunwoo Jeon
Student ID: 2024148005
Lab problem: lab12_p3.py
"""

#
# This program encrypt or decrypt the file using random key.
#

from random import random

characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
              "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
              "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d",
              "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
              "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
              "y", "z", "0", "1", "2", "3", "4", "5", "6", "7",
              "8", "9", " ", "."]
key_characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
              "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
              "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d",
              "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
              "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
              "y", "z", "0", "1", "2", "3", "4", "5", "6", "7",
              "8", "9", " ", "."]

file = input("Enter a filename: ")
filename = file.split(".")[0]
file_extension = file.split(".")[-1]

if file_extension == "txt":
    key = {}
    counter = 0
    while len(key_characters) > 0:
        key[characters[counter]] = key_characters.pop(int(random()*len(key_characters)))
        counter += 1
    key["="] = "="
    key["\n"] = "\n"

    try:
        original_file = open(file, "r")
    except FileNotFoundError:
        raise FileNotFoundError("Cannot open the file")

    enc_file = open(filename + ".enc", 'w')
    for line in original_file:
        for char in line:
            enc_file.write(key[char])
    original_file.close()
    enc_file.close()

    key_file = open(filename + ".key", 'w')
    for char in characters:
        key_file.write(f"{char},{key[char]}\n")
    key_file.write("=,=")
    key_file.close()
elif file_extension == "enc":
    try:
        key_file = open(filename + ".key", 'r')
    except FileNotFoundError:
        raise FileNotFoundError("Cannot open the file")

    key = {}
    for line in key_file:
        key[line.split(",")[1][0]] = line.split(",")[0]
    key_file.close()

    enc_file = open(filename + ".enc", 'r')
    dec_file = open(filename + ".txt", 'w')
    for line in enc_file:
        for char in line:
            if char != "\n":
                dec_file.write(key[char])
            else:
                dec_file.write("\n")
    enc_file.close()
    dec_file.close()
