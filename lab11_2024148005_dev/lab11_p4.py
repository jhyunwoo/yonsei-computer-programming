import math  # Import the math module for mathematical operations

def openFiles():
    '''
        Prompts the user for the file names to open, opens the files,
        and returns the file objects for each in a tuple of the form
        (air_pollution_datafile, cancer_datafile).

        Raises an OSError exception if the files are not successfully
        opened after four attempts of entering file names.
    '''

    lung_cancer_opened = False  # Flag to check if the lung cancer data file is opened
    air_pollution_opened = False  # Flag to check if the air pollution data file is opened
    num_attempts = 4  # Number of allowed attempts to open files

    # Loop to prompt for file names and attempt to open files
    while ((not lung_cancer_opened) or (not air_pollution_opened)) and (num_attempts > 0):
        try:
            if not lung_cancer_opened:
                file_name = input('Enter lung cancer data from filename: ')  # Prompt user for lung cancer data file name
                cancer_datafile = open(file_name, 'r')  # Open the lung cancer data file
                lung_cancer_opened = True  # Set flag to true if the file is opened successfully

            if not air_pollution_opened:
                file_name = input('Enter air pollution data from filename: ')  # Prompt user for air pollution data file name
                pollution_datafile = open(file_name, 'r')  # Open the air pollution data file
                air_pollution_opened = True  # Set flag to true if the file is opened successfully

        except OSError:
            # If the file is not found, inform the user and decrease the number of attempts
            print('File not found:', file_name + '.', 'Please reenter\n')
            num_attempts -= 1  # Decrement the number of attempts

    # If one or more files are not opened after allowed attempts, raise an OSError exception
    if not lung_cancer_opened or not air_pollution_opened:
        raise OSError('Too many attempts of reading input files')

    # Return the file objects if both are successfully opened
    else:
        return (cancer_datafile, pollution_datafile)


def checkHasSameState(list1, list2):
    '''
        Ensures that both lists have the same states for data correlation
        by finding matching states in both lists, creating new lists with only these states,
        and returning the sorted new lists.
    '''
    new_list1 = []  # New list to store matching states from the first list
    new_list2 = []  # New list to store matching states from the second list
    for i in range(len(list1)):  # Loop through the first list
        for j in range(len(list2)):  # Loop through the second list
            if list1[i][0].lower() == list2[j][0].lower():  # If the state names match (case insensitive)
                new_list1.append(list1[i])  # Add the matching state data to the new first list
                new_list2.append(list2[j])  # Add the matching state data to the new second list
    new_list1.sort()  # Sort the new first list
    new_list2.sort()  # Sort the new second list
    return (new_list1, new_list2)  # Return the sorted new lists


def readFiles(cancer_datafile, pollution_datafile):
    '''
        Reads the data from the provided file objects air_pollution_datafile
        and cancer_datafile. Returns a list of the data read from each
        in a tuple of the form (air_pollution_data, cancer_data).
    '''

    cancer_data = []  # List to store lung cancer data
    pollution_data = []  # List to store air pollution data
    empty_str = ''  # Empty string for comparison

    cancer_datafile.readline()  # Skip the header line in the lung cancer data file
    pollution_datafile.readline()  # Skip the header line in the air pollution data file

    eof = False  # Flag to check if end of file is reached
    while not eof:
        c_line = cancer_datafile.readline()  # Read a line from the lung cancer data file
        p_line = pollution_datafile.readline()  # Read a line from the air pollution data file

        if c_line == empty_str and p_line == empty_str:  # Check if end of both files is reached
            eof = True  # Set flag to true if end of both files is reached
        else:
            # Append the read data to respective lists, splitting and stripping each line
            cancer_data.append(c_line.strip().split(','))  # Add lung cancer data to the list
            pollution_data.append([p_line.strip().split(',')[1], p_line.strip().split(',')[2]])  # Add air pollution data to the list

    # Ensure both lists contain data for the same states and return them
    cancer_data, pollution_data = checkHasSameState(cancer_data, pollution_data)
    return (cancer_data, pollution_data)  # Return the lists of data


def calculateCorrelation(pollution_data, cancer_data):
    '''
        Calculates and returns the correlation value for the data
        provided in lists pollution_data and cancer_data.
    '''

    sum_pollution_vals = sum_cancer_vals = 0  # Initialize sums of values
    sum_pollution_sqrd = sum_cancer_sqrd = 0  # Initialize sums of squared values
    sum_products = 0  # Initialize sum of products of corresponding values

    num_values = len(pollution_data)  # Get the number of data points

    # Calculate sums of values, squared values, and products of corresponding values
    for k in range(num_values):
        sum_pollution_vals += float(pollution_data[k][1])  # Add to the sum of pollution values
        sum_cancer_vals += float(cancer_data[k][1])  # Add to the sum of cancer values

        sum_pollution_sqrd += float(pollution_data[k][1]) ** 2  # Add to the sum of squared pollution values
        sum_cancer_sqrd += float(cancer_data[k][1]) ** 2  # Add to the sum of squared cancer values

        sum_products += float(pollution_data[k][1]) * float(cancer_data[k][1])  # Add to the sum of products

    # Calculate the numerator for the correlation formula
    numer = (num_values * sum_products) - (sum_pollution_vals * sum_cancer_vals)
    # Calculate the denominator for the correlation formula
    denom = math.sqrt(abs(((num_values * sum_pollution_sqrd) - (sum_pollution_vals ** 2)) *
                          ((num_values * sum_cancer_sqrd) - (sum_cancer_vals ** 2))))

    return numer / denom  # Return the correlation coefficient


# ---- main

print('This program will determine the correlation (-1 to 1) between')  # Display program description
print('data on air pollution and incidences of lung cancer\n')  # Display program description

try:
    lung_cancer_datafile, air_pollution_datafile = openFiles()  # Open data files

    lung_cancer_data, air_pollution_data = readFiles(lung_cancer_datafile, air_pollution_datafile)  # Read data from files

    correlation = calculateCorrelation(lung_cancer_data, air_pollution_data)  # Calculate the correlation coefficient

    print('r_value = ', correlation)  # Display the correlation coefficient

except OSError as e:
    # Handle file opening errors and terminate the program
    print(e)  # Print the error message
    print('Program terminated ...')  # Indicate that the program has terminated
