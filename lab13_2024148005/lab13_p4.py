"""
Name: Hyunwoo Jeon
Student ID: 2024148005
Lab problem: lab13_p4.py
"""

#
# This program contains fib function that
# calculate fibonacci sequence using recursive function
#

def fib(n):
    """
    Recursively computes the n-th Fibonacci number.

    :param n : The position in the Fibonacci sequence to compute. Must be a non-negative integer.

    :return The n-th Fibonacci number.
    """
    if n <= 0:
        # Base case: the 0th Fibonacci number is 0
        return 0
    elif n == 1:
        # Base case: the 1st Fibonacci number is 1
        return 1
    else:
        # Recursive case: sum of the two preceding Fibonacci numbers
        return fib(n-1) + fib(n-2)
    
