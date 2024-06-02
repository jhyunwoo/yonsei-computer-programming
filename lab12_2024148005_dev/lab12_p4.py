"""
Name: Hyunwoo Jeon
Student ID: 2024148005
Lab problem: lab12_p4.py
"""

#
# This program Fraction class that have some utilities
#

def gcd(a, b):
    """
    This function returns the greatest common divisor of a and b.
    :param a: int type
    :param b: int type
    :return: gcd of a and b
    """
    # Variable that store gcd
    gcd = None

    # Use Euclid Algorithm to find GCD
    c = a % b  # Variable for calculate GCD

    if c != 0:  # if c is not 0, b assign to a, c assign to b
        a = b
        b = c
    else:  # else, GCD is b
        gcd = b

    # Find GCD when c is not 0
    while c != 0:
        c = a % b
        if c != 0:  # if c is not 0, b assign to a, c assign to b
            a = b
            b = c
        else:  # else, GCD is b
            gcd = b
    return gcd


#
# Fraction class:
#

# Class that calculating Fraction
class Fraction(object):
    """
    Class to represent a number as a fraction

    Examples: 1/2, 2/5
    """

    def __init__(self, n, d):
        """ Method to construct a Fraction object """
        # Check that n and d are of type int:
        if type(n) != int or type(d) != int:  # Check the type of n and d
            raise ValueError('requires type int')  # if n or d type is incorrect, raise ValueError
        # Check that denominator is non-zero:
        if d == 0:  # if d is 0, raise ZeroDivisionError
            raise ZeroDivisionError('requires non-zero denominator')
        # If we get here, n and d are ok => initialize Fraction:
        self.num = n  # Assign n value to num variable
        self.denom = d  # Assign d value to the denom variable
        self.reduce()  # Call reduce function for reduce fraction

    def __str__(self):
        """ Returns a string representation of the fraction object (self) """
        return str(self.num) + '/' + str(self.denom)

    def __mul__(self, other):
        """ Returns new Fraction representing self * other """
        new_num = self.num * other.num  # Multiply num and input num
        new_denom = self.denom * other.denom  # Multiply denom and input denom
        return Fraction(new_num, new_denom)  # Create new Fraction class using multiplied variable

    def __add__(self, other):
        """ Returns new Fraction representing self + other """
        new_num = self.num * other.denom + other.num * self.denom  # Create new_num using added value
        new_denom = self.denom * other.denom  # Create new_denom using added value
        return Fraction(new_num, new_denom)  # Create new Fraction class using added variable

    def __float__(self):
        """ Returns a float-value of the Fraction object """
        return self.num / self.denom  # result of / is of type float

    def reduce(self):
        """
        Reduces self to simplest terms.
        This is done by dividing both numerator and denominator by their greatest common divisor (GCD).
        Also removes the signs if both numerator and denominator are negative.
        Whole numbers (1, 2, ...) are represented as 1/1, 2/1, 3/1, ...
        """
        gcd_value = gcd(self.num, self.denom)  # Get GCD of num and denom value using gcd function
        if type(self.num / gcd_value) is int and type(self.denom / gcd_value) is int:  # if num and denom type is int
            self.num = int(self.num / gcd_value)  # Assign as int type
            self.denom = int(self.denom / gcd_value)  # Assign as int type
        else:  # if num or denom is not int type
            self.num = self.num / gcd_value  # Assign calculated value
            self.denom = self.denom / gcd_value  # Assign calculated value

    def adjust(self, factor):
        """Multiplies numerator and denominator by factor."""
        self.num = self.num * factor  # Assign num with multiplied by factor
        self.denom = self.denom * factor  # Assign denom with multiplied by factor
