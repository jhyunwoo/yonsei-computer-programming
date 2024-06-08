"""
Name: Hyunwoo Jeon
Student ID: 2024148005
Lab problem: lab13_p1.py
"""

#
# This program contains Range class that control range
#


class Range:
    """
    Class to represent a range
    This Range class include special method __lt__
    Also, if call special method __str__,
    it will return the string representation of the range
    """
    def __init__(self, start, end):
        """
        Initialize the range
        start is should be less than end
        :param start: start of the range
        :param end: end of the range
        """
        if start > end:  # If start is greater than end
            raise IndexError  # Raise index error
        self.__start = start  # Variable that contains start value
        self.__end = end  # Variable that contains end value

    def __str__(self):
        """
        If program call __str__,
        it will return the string representation of the range
        :return: string representation of the range
        """
        # Return string representation of the range
        return f'{self.__start}...{self.__end}'

    def __lt__(self, other):
        """
        Special method that checks
        if all elements of range are less than the other
        :param other: Range Class
        :return: Boolean
        """
        # if all elements of range is less than other range, return True
        return self.__end < other.__start

