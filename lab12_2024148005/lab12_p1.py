"""
Name: Hyunwoo Jeon
Student ID: 2024148005
Lab problem: lab12_p1.py
"""

#
# This program get dict, day and temperature and if dict does not have day,
# add day and temperature on dict
#


def addDailyTemp(mydict, day, temperature):
    """
    Add key 'day' and value 'temperature' to the dictionary 'mydict',
    only if key 'day' does not already exist in the dictionary.
    The resulting dictionary is returned.
    """
    if day not in mydict:  # if day is not in mydict
        mydict[day] = temperature  # add day and temperature on mydict

    return mydict  # Return mydict
