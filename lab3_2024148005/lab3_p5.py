#
# This program calculates the difference in seconds between the birth dates of two people.
# Fist, I used 1900 January 1st as reference point and calculate gap between birth date of people.
# Second, Calculate gap second between two people.
# Last, print result of this program.
#

# Get Person 1 birth information
person1_month = int(input("Person 1: Enter month born (1-12): "))
person1_day = int(input("Person 1: Enter day born (1-31): "))
person1_year = int(input("Person 1: Enter year born (4-digit): "))
# Get Person 2 birth information
person2_month = int(input("Person 2: Enter month born (1-12): "))
person2_day = int(input("Person 2: Enter day born (1-31): "))
person2_year = int(input("Person 2: Enter year born (4-digit): "))

# Setting constants to calculate result
numsecs_day = 24 * 60 * 60
numsecs_year = 365 * numsecs_day
avg_numsecs_year = (4 * numsecs_year + numsecs_day) // 4
avg_numsecs_month = avg_numsecs_year // 12

# Calculate differences from January 1 1900 both person 1 and person 2
numsecs_1900_person1 = (person1_year - 1900) * avg_numsecs_year + (person1_month - 1) * avg_numsecs_month + (person1_day * numsecs_day)

numsecs_1900_person2 = (person2_year - 1900) * avg_numsecs_year + (person2_month - 1) * avg_numsecs_month + (person2_day * numsecs_day)

# Print result (using
print('Age difference in seconds:', abs(numsecs_1900_person1 - numsecs_1900_person2))
