def modCount(n, m):
    """
    This function get two integers and calculate how many numbers that can divide n by m.
    :param n: integer
    :param m: integer
    :return: integer
    """
    divider = 0
    while m >= 1:  # Find how many numbers that can divide n by m
        if n % m == 0:
            divider += 1
        m -= 1

    return divider

