def scalar_dif(y, A):
    """
    This function get integer y and Matrix A. Calculate the scalar dif between y and A.
    :param y: integer except 0
    :param A: matrix
    :return: matrix
    """
    res = []  # Final Result Matrix

    for row in A:
        res_row = []  # Row result Matrix
        for num in row:
            res_row.append(num/y)  # Divide by y and append to res_row
        res.append(res_row)  # Append to res

    return res
