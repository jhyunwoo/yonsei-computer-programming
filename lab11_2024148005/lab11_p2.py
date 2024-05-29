def newItem(item: str, cost: int, outputFile: str):
    """
    Takes an item and its cost, and appends them to a text file called outputFile.
    If item or cost are invalid, or outputFile cannot be opened, then ValueError is thrown.
    Otherwise, the first two data are appended to outputFile separated by a comma, and 0 is returned.

    Parameters:
    item (str): The name of the item.
    cost (int): The cost of the item.
    outputFile (str): The name of the output file where the item and cost will be appended.

    Returns:
    int: 0 if the operation is successful.

    Raises:
    ValueError: If item or cost are invalid, or if the file cannot be opened.
    """

    # Check if the item is an empty string, longer than 50 characters, or has more than 2 words.
    if not item or len(item) > 50 or len(item.split()) > 2:
        raise ValueError("Invalid argument")  # Raise a ValueError if any of the item conditions are not met

    # Check if the cost is less than 0 or greater than 999,999,999,999.
    if cost < 0 or cost > 999_999_999_999:
        raise ValueError("Invalid argument")  # Raise a ValueError if the cost is outside the valid range

    try:
        # Try to open the output file in append mode.
        file = open(outputFile, 'a')

        # Write the item and cost to the file, separated by a comma and followed by a newline.
        file.write(item + "," + str(cost) + '\n')

        # Close the file after writing.
        file.close()
    except OSError:
        # Raise a ValueError if there is an issue opening or writing to the file.
        raise ValueError("File append error")

    return 0  # Return 0 to indicate successful completion of the function
