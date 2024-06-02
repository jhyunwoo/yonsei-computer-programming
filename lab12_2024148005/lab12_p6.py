"""
Name: Hyunwoo Jeon
Student ID: 2024148005
Lab problem: lab12_p6.py
"""


class IntCounter:
    def __init__(self):
        self.count_value = 0
        self.total_value = 0

    def insert(self, value):
        if type(value) is int:
            self.count_value += 1
            self.total_value += value
        elif type(value) is float and value.is_integer():
            self.count_value += 1
            self.total_value += value
        elif type(value) is str and value.isdecimal():
            self.count_value += 1
            self.total_value += int(value)

    def count(self):
        if float(self.count_value).is_integer():
            return int(self.count_value)
        else:
            return self.count_value

    def total(self):
        if float(self.total_value).is_integer():
            return int(self.total_value)
        else:
            return self.total_value


