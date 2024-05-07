def ordered3(a, b, c):
    """
    This function get three int type variables, and check order is smallest to largest
    :param a: integer
    :param b: integer
    :param c: integer
    :return: Boolean
    """
    if a <= b <= c:  # if a, b, c is order by smallest to largets, return True
        return True
    else:  # else return False
        return False

