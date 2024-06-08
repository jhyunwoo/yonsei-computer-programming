"""
Name: Hyunwoo Jeon
Student ID: 2024148005
Lab problem: lab13_p6.py
"""

#
# This program contains fibcalls function that
# calculate how many recursive function call when calculating fibonacci sequence
#

def fibcalls(n):
    """
    Recursively computes the number of function calls required to compute the n-th Fibonacci number.

    :param n The position in the Fibonacci sequence for which to count the function calls. Must be a non-negative integer.
    :return The number of function calls required to compute the n-th Fibonacci number.
    """

    # Base case: If n is 0 or 1, only one call is needed
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: sum of calls for (n-1) and (n-2), plus 1 for the current call
        return fibcalls(n-1) + fibcalls(n-2) + 1
