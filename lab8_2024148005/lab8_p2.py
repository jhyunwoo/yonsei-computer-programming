def removeValuesInPlace(L, threshold):
    """
    This function get list L and threshold value and delete value of list which above threshold value.
    :param L: integer list
    :param threshold: integer
    :return: integer list
    """
    length = len(L) - 1  # Length of input list L and minus 1
    for i in range(length, -1, -1):  # for loop for check each values in list
        if L[i] > threshold:  # if L[length-i] is above than threshold, delete value in the list
            L.pop(i)
    return L  # Return mutated list

