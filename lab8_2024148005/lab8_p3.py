def increaseValues(L, threshold):
    """
    This function increase values which are below than threshold
    :param L: integer list
    :param threshold: integer value
    :return: integer list
    """
    Result = []  # Variable that store list of integers
    for i in range(len(L)):  # For loop to check all values in L
        if L[i] < threshold:  # If variable in L is below than threshold, append increased variable in Result List
            Result.append(L[i]+1)
        else:  # Else, append original value
            Result.append(L[i])
    return Result  # Return Result List

