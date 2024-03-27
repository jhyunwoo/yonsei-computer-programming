#
# This program get ean code from user and generate validation code.
# To get EAN code's each digit, I convert user input to int type and calculate each digit using % and //.
#

# Get EAN code
ean = int(input("Enter the first 12 digits of an EAN: "))

# Get each digit from user input
digit_12 = ean % 10
digit_11 = ean//10 % 10
digit_10 = ean//100 % 10
digit_9 = ean//1_000 % 10
digit_8 = ean//10_000 % 10
digit_7 = ean//100_000 % 10
digit_6 = ean//1_000_000 % 10
digit_5 = ean//10_000_000 % 10
digit_4 = ean//100_000_000 % 10
digit_3 = ean//1_000_000_000 % 10
digit_2 = ean//10_000_000_000 % 10
digit_1 = ean//100_000_000_000 % 10

# Calculate Validation Code
first_sum = digit_2 + digit_4 + digit_6 + digit_8 + digit_10 + digit_12
second_sum = digit_1 + digit_3 + digit_5 + digit_7 + digit_9 + digit_11

result = 9-((first_sum * 3 + second_sum - 1) % 10)

# Print Result
print("Check digit:", result)

# Simplified Code

# # Get EAN code
# ean = input("Enter the first 12 digits of an EAN: ")
#
#
# # Calculate Validation Code
# first_sum = int(ean[1]) + int(ean[3]) + int(ean[5]) + int(ean[7]) + int(ean[9]) + int(ean[11])
# second_sum = int(ean[0]) + int(ean[2]) + int(ean[4]) + int(ean[6]) + int(ean[8]) + int(ean[10])
#
# result = 9-((first_sum * 3 + second_sum - 1) % 10)
#
# # Print Result
# print("Check digit:", result)
