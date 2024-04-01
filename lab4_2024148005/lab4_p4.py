#
# This program print integer 1-100 using for loop.
#

# Print 1 - 100
for i in range(1, 101):
    if i % 10 == 0:  # if i%10 is 0, print with enter
        print(format(i, ">3"))
    else:  # else print without enter
        print(format(i, ">3"), end="")
