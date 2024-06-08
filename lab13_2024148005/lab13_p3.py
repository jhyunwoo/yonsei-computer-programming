"""
Name: Hyunwoo Jeon
Student ID: 2024148005
Lab problem: lab13_p3.py
"""

#
# This program contains auto_doboggi_man that get all doboggi automatically
#

# Import our own constants:
from globals import FOODMAX, STEPMAX, WIDTH, HEIGHT, X_MAX, Y_MAX, MS_TO_QUIT
from globals import FOOD as food, GHOSTS as ghosts

# Import our own doboggi_man class:
from characters import doboggi_man

import turtle


class auto_doboggi_man(doboggi_man):
    """
    Class auto_doboggi_man, the autonomous doboggi-collector.

    The auto_doboggi_man class is a subclass of the doboggi_man class.
    It inherits all data attributes and methods from the doboggi_man class.
    It overrides the move() method of the doboggi_man class to automatically
    navigate doboggi_man across the screen.

    Attributes:
    target : list
        A list of target positions (coordinates) for the auto_doboggi_man to move towards.
    danger : bool
        A flag indicating whether the auto_doboggi_man is in danger of encountering a ghost.
    """

    def __init__(self, x, y):
        """
        Initializes the auto_doboggi_man with a starting position and default attributes.

        :param x The initial x-coordinate of the auto_doboggi_man.
        :param y The initial y-coordinate of the auto_doboggi_man.
        """
        super().__init__(x, y)  # Initialize parent class
        self.target = []  # Initialize an empty list to store target positions
        self.danger = False  # Initialize the danger flag to False

    def in_danger(self):
        """
        Checks if the auto_doboggi_man is in danger of encountering a ghost.

        :return True if the auto_doboggi_man is in danger, False otherwise.
        """
        danger = False  # Initialize the local danger flag to False

        if self.dir == "north":  # Check for danger if moving north
            for ghost in ghosts:  # Iterate over all ghosts
                ghost_pos = ghost.getPosition()
                my_pos = self.getPosition()

                # Check vertical distance and horizontal proximity to detect danger
                if 10 < ghost_pos[1] - my_pos[1] < 100 and\
                        abs(ghost_pos[0] - my_pos[0]) < 100:
                    danger = True

                # Additional check for wrap-around danger scenario
                if my_pos[0] < 0 and \
                        WIDTH / 2 - ghost_pos[0] + (WIDTH / 2 + my_pos[0]) < 100:
                    danger = True

        return danger  # Return the danger status

    def move(self):
        """
        Automatically moves the auto_doboggi_man towards
        the nearest food target while avoiding danger.
        """
        if not self.target:  # Check if there are no targets
            for food_item in food:  # Iterate over all food items
                # Append food positions to targets
                self.target.append(food_item.getPosition())
            # Sort targets by their y-coordinate
            self.target.sort(key=lambda z: z[1])

        current_pos = self.getPosition()

        # Check if the current position matches the first target position
        if current_pos[0] == self.target[0][0] and current_pos[1] == self.target[0][1]:
            self.target.pop(0)  # Remove the reached target from the list

        if not self.in_danger():  # Proceed if not in danger
            # Check if the x-coordinate does not match
            if current_pos[0] != self.target[0][0]:
                gap = self.target[0][0] - current_pos[0]
                if gap < 0:
                    self.turnWest()  # Turn west if the gap is negative
                else:
                    self.turnEast()  # Turn east if the gap is positive

                # Move forward by a maximum of 10 units
                # or the gap distance, whichever is smaller
                self.ttl.forward(min(10, abs(gap)))
            # Check if the y-coordinate does not match
            elif current_pos[1] != self.target[0][1]:
                gap = self.target[0][1] - current_pos[1]
                if gap < 0:
                    self.turnSouth()  # Turn south if the gap is negative
                else:
                    self.turnNorth()  # Turn north if the gap is positive

                # Move forward by a maximum of 10 units or the gap distance, whichever is smaller
                self.ttl.forward(min(10, abs(gap)))
