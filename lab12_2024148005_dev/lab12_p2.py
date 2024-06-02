"""
Name: Hyunwoo Jeon
Student ID: 2024148005
Lab problem: lab12_p2.py
"""

#
# This program filter average temperature
#

def moderateDays(mydict):
    """
    Returns a list of the days for which the average temperature
    was between 70 and 79 degrees.
    """
    # Define a tuple containing the days of the week.
    days = ("Sun", 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')
    # Initialize an empty list to store the filtered results.
    filtered = []

    # Iterate over each day in the days tuple.
    for day in days:
        # Check if the average temperature for the current day is between 70 and 79 degrees inclusive.
        if 79 >= mydict[day] >= 70:
            # If the condition is met, add the current day to the filtered list.
            filtered.append(day)
    # Return the list of filtered days.
    return filtered
