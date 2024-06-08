"""
Name: Hyunwoo Jeon
Student ID: 2024148005
Lab problem: lab13_p2.py
"""

#
# This program contains AvgList class
# that extend from list class and add computeAvg method
#


class AvgList(list):
    """
    A subclass of list that only allows appending integers and floats,
    and provides a method to compute the average of the elements.

    Methods:
    append(__object): Appends an integer or float to the list.
        Raises ValueError for other types.
    computeAvg(): Computes and returns the average
        of the elements in the list.
    """

    def append(self, __object):
        """
        Appends an integer or float to the list.
        Raises ValueError for other types.

        :param __object : int or float that the object to append to the list.
        :raise ValueError if __object is not an integer or float.
        """
        if not isinstance(__object, int) and not isinstance(__object, float):
            raise ValueError("Only integers and floats are allowed.")
        # Use the superclass append method to add the element
        super().append(__object)

    def computeAvg(self):
        """
        Computes and returns the average of the elements in the list.

        :return float that represents the average of the elements in the list.
        :raise ZeroDivisionError if __object is not an integer or float.
        """
        if len(self) == 0:  # if length is 0, raise zero division E
            raise ZeroDivisionError("Cannot compute average of an empty list.")

        list_sum = 0  # Initialize the sum of the list elements
        for i in range(len(self)):
            list_sum += self[i]  # Add each element to the sum

        return list_sum / len(self)  # Return the average of the elements


