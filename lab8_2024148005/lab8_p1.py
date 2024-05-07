def increaseValuesInPlace(L, threshold):
    """
    Increase the value of L which is less than the threshold.
    :param L: list of numbers
    :param threshold: int
    :return: mutated list L
    """
    for i in range(0, len(L)):  # for loop for check all values in list L
        if L[i] < threshold:  # if value is less than threshold, increase the value
            L[i] = L[i] + 1
    return L  # Return L

