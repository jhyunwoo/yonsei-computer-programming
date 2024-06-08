"""
Name: Hyunwoo Jeon
Student ID: 2024148005
Lab problem: lab13_p8.py
"""

#
# This program contains MedianSet class
# that computes the median of a set of unique numeric values.
#


class MedianSet(set):
    """
    Computes the median of a set of unique numeric values.
    Raises a ValueError when any element is not a numeric value.
    Returns the middle if the number of elements are odd.
    Returns the mean of the middle two if the number of elements is even.

    Methods:
    computeMedian():
        Computes and returns the median of the set's numeric values.
        Raises a ValueError if any element is not a numeric value.
    """

    def computeMedian(self):
        """
        Computes the median of a set of unique numeric values.

        :return The median of the set's numeric values.

        :raise ValueError if any element in the set is not a numeric value.
        """
        converted_list = []  # Initialize an empty list to store numeric values
        for element in self:
            try:
                # Try to convert the element to a float and append it to the list if it's not already present
                if not float(element) in converted_list:
                    converted_list.append(float(element))
            except ValueError:
                # Raise a ValueError if the element cannot be converted to a float
                raise ValueError("All elements must be numeric values.")

        converted_list.sort()  # Sort the list of numeric values in ascending order

        n = len(converted_list)  # Get the number of elements in the list
        if n % 2 == 0:
            # If the number of elements is even, compute the mean of the two middle values
            median = (converted_list[n // 2] + converted_list[n // 2 - 1]) / 2
        else:
            # If the number of elements is odd, return the middle value
            median = converted_list[n // 2]

        return median  # Return the computed median
