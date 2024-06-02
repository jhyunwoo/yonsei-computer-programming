"""
Name: Hyunwoo Jeon
Student ID: 2024148005
Lab problem: lab12_p5.py
"""

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

    def __str__(self):
        """ Returns a string representation of the fraction object (self) """
        return str(self.num) + '/' + str(self.denom)

    def __mul__(self, other):
        """ Returns new Fraction representing self * other """
        if type(other) is int and type(other) is int:
            return Fraction(self.num * other, self.denom)
        elif type(other) is Fraction:
            return Fraction(self.num * other.num, self.denom * other.denom)
        else:
            raise ValueError("value error")

    def __add__(self, other):
        """ Returns new Fraction representing self + other """
        if type(other) is int and type(other) is int:
            return Fraction(self.num + (self.denom * other), self.denom)
        elif type(other) is Fraction:
            return Fraction(self.num * other.denom + other.num * self.denom, self.denom * other.denom)
        else:
            raise ValueError("value error")

    def __float__(self):
        """ Returns a float-value of the Fraction object """
        return self.num / self.denom  # result of / is of type float
