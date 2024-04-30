# Get ISBN from user
isbn = input("Enter an ISBN: ")
# Split ISBN by dash
isbn = isbn.split("-")

# Print Result using format method
print("{:.<20}GS1 prefix".format(isbn[0]))
print("{:.<20}Group identifier".format(isbn[1]))
print("{:.<20}Publisher code".format(isbn[2]))
print("{:.<20}Item number".format(isbn[3]))
print("{:.<20}Check digit".format(isbn[4]))
