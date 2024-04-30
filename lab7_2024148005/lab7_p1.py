def zeroCheck(a, b, c):
    """
    This function get three variables and  checks if a, b and c are zero
    :param a: integer
    :param b: integer
    :param c: integer
    :return: Boolean Value
    """
    if not (a and b and c):  # if any input value is 0, return True
        return True
    else:
        return False