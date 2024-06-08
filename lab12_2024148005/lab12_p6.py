"""
Name: Hyunwoo Jeon
Student ID: 2024148005
Lab problem: lab12_p6.py
"""


#
# This program provide IntCounter class
#


# Class that count int
class IntCounter:
    def __init__(self):
        """ Initial count_value and total_value """
        self.count_value = 0
        self.total_value = 0

    def insert(self, value):
        """ Function that insert value on IntCounter Class"""
        if type(value) is int:  # If type of value is int
            self.count_value += 1  # Increment count_value
            self.total_value += value  # Add value to the total_value
        # if value is float type and value is convertable to int type
        elif type(value) is float and value.is_integer():
            self.count_value += 1  # Increment count_value
            self.total_value += value  # Add value to the total_value
        # if value is str type and it can convert to int type
        elif type(value) is str and value.isdecimal():
            self.count_value += 1  # Increment count_value
            self.total_value += int(value)  # Add value to the total_value

    def count(self):
        """ Return count value """
        # if count_value can represent as int type
        if float(self.count_value).is_integer():
            # Convert count_value to int and return it
            return int(self.count_value)
        else:  # if count_value is not convert to int type
            return self.count_value  # Return count value

    def total(self):
        """ Return total value """
        # if total_value can represent as int type
        if float(self.total_value).is_integer():
            # Convert total_value to int and return it
            return int(self.total_value)  
        else:  # if total_value is not convert to int type
            return self.total_value  # Return total value
