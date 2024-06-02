"""
Name: Hyunwoo Jeon
Student ID: 2024148005
Lab problem: lab12_p4.py
"""


def gcd(a, b):
    # Variable that store gcd
    gcd = None

    # Use Euclid Algorithm to find GCD
    c = a % b

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


class Fraction(object):
    """
    Class to represent a number as a fraction

    Examples: 1/2, 2/5
    """

    def __init__(self, n, d):
        """ Method to construct a Fraction object """
        # Check that n and d are of type int:
        if type(n) != int or type(d) != int:
            raise ValueError('requires type int')
        # Check that denominator is non-zero:
        if d == 0:
            raise ZeroDivisionError('requires non-zero denominator')
        # If we get here, n and d are ok => initialize Fraction:
        self.num = n
        self.denom = d
        self.reduce()

    def __str__(self):
        """ Returns a string representation of the fraction object (self) """
        return str(self.num) + '/' + str(self.denom)

    def __mul__(self, other):
        """ Returns new Fraction representing self * other """
        new_num = self.num * other.num
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)

    def __add__(self, other):
        """ Returns new Fraction representing self + other """
        new_num = self.num * other.denom + other.num * self.denom
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)

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
        gcd_value = gcd(self.num, self.denom)
        if type(self.num) is int and type(self.denom) is int:
            self.num = int(self.num / gcd_value)
            self.denom = int(self.denom / gcd_value)
        else:
            self.num = self.num / gcd_value
            self.denom = self.denom / gcd_value

    def adjust(self, factor):
        """Multiplies numerator and denominator by factor."""
        self.num = self.num * factor
        self.denom = self.denom * factor
