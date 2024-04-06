#
# This program count how many vowels in the sentence.
#

# Get sentence from user input
sentence = input("Enter a sentence: ")
# Convert capital letters to lower case
sentence = sentence.lower()

# Count all vowels in the sentence
count = 0
count += sentence.count("a")
count += sentence.count("e")
count += sentence.count("i")
count += sentence.count("o")
count += sentence.count("u")

# Print result
if count == 1:
    print(f"Your sentence contains {count} vowel.")
else:
    print(f"Your sentence contains {count} vowels.")
