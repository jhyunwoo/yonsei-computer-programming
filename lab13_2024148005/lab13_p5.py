"""
Name: Hyunwoo Jeon
Student ID: 2024148005
Lab problem: lab13_p5.py
"""

#
# This program contains fib_memo function that
# calculate fibonacci sequence using recursive function and memoization
#

# Initialize a dictionary to store previously computed Fibonacci numbers
memo = {}

def fib_memo(n):
    """
    Recursively computes the n-th Fibonacci number using memoization.

    :param n The position in the Fibonacci sequence to compute. Must be a non-negative integer.
    :return The n-th Fibonacci number.
    """

    # Base case: the 0th Fibonacci number is 0
    if n <= 0:
        return 0
    # Base case: the 1st Fibonacci number is 1
    elif n == 1:
        return 1

    # Check if the value has already been computed and is stored in the memo dictionary
    if n in memo:
        return memo[n]
    else:
        # Compute the n-th Fibonacci number and store it in the memo dictionary
        memo[n] = fib_memo(n - 2) + fib_memo(n - 1)

    # Return the computed Fibonacci number from the memo dictionary
    return memo[n]