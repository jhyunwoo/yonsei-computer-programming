#
# This program get data from 'data.txt' file and calculate smoothed list.
#

# Open the file "data.txt" in read mode
data_file = open("data.txt", 'r')

# Initialize an empty list to store the data read from the file
data_list = []

# Read all lines from the file
data = data_file.readlines()

# Iterate over each line read from the file
for line in data:
    # Convert the line to a float and remove the newline character at the end
    data_list.append(int(line.strip()))

# Add the first element at the beginning and the last element at the end of the list
data_list = [data_list[0]] + data_list + [data_list[-1]]

# Initialize an empty list to store the smoothed data
smoothed_data = []

# Iterate over the data list, excluding the first and last padded elements
for i in range(len(data_list) - 2):
    # Calculate the average of the current element and its two neighbors
    smoothed_data.append((data_list[i] + data_list[i + 1] + data_list[i + 2]) / 3)

# Print the smoothed data
print(smoothed_data)