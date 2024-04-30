def evalPolynomial(x, L):
    """
    This function get integer x and list of integers L, calculate polynomials of degree L
    :param x: integer
    :param L: List of integers
    :return: integer
    """
    result = 0
    for i in range(len(L)):
        result += L[i] * x ** i  # Calculate polynomials

    return result
