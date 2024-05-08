def lookAndSay(n, i):
    """
    This function get positive integer n and i for how many times to look and say n integer.
    return if this look and say process have cycle
    :param n: positive integer
    :param i: positive integer
    :return: boolean if this look and say process have cycle
    """
    # Convert int to list of str
    look_list = list(map(int, str(n)))
    final_result = []  # Store all process

    # Print first n
    print("1:", n)
    # For loop for look and say look_list i times
    for j in range(i-1):
        say_list = []  # store how many variables in the list
        elements = []  # Get which numbers in list
        for look in look_list:  # Check all variables in list
            if elements.count(look) == 0:  # if elements list do not have look variable, append to it
                elements.append(look)
        elements.sort()  # Sort elements list

        for element in elements:  # Count how many element in look_list and append to say_list
            say_list.append([look_list.count(element), element])

        int_list_to_str = ''.join(str(x) for x in sum(say_list, []))  # Convert int list to str type
        print(f"{j+2}:", int_list_to_str)  # Print result
        final_result.append(int_list_to_str)  # Append result to final_result
        look_list = sum(say_list, [])  # init look_list to say_list

    cycle = False  # Check this look and say process have cycle
    check_length = 1  # Grop length of cycle

    # Check if look and say process have cycle
    for _ in range(len(final_result)):
        for k in range(0, len(final_result), check_length):
            if k < len(final_result)-check_length:
                check_value = ""  # Variable for check this process have cycle
                for i in range(check_length):
                    check_value += final_result[k + i]  # Add to check_value for check_length times
                if final_result[k] == final_result[k+check_length]:  # If final_result have cycle, update cycle variable
                    cycle = True
        check_length += 1

    # Return cycle
    return cycle
