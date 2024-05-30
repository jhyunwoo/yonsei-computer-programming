#
# This program is cellular automaton and show on python turtle
#

import time  # Import time module for delaying the output
import turtle

SIZE = 20  # Size of the 2D cellular automaton grid
work = []  # List to store the current generation grid
tmp = []  # Temporary list for processing the next generation



def next_generation(world):
    '''Calculate the next generation of the world grid.'''
    new_world = []  # Initialize a new list for the next generation
    for p in range(len(world)):  # Loop through each row in the grid
        new_row = []  # Initialize a new list for the new row
        for m in range(len(world[p])):  # Loop through each cell in the row
            live_cell = 0  # Counter for live cells around the current cell
            for n in range(3):  # Loop through the 3x3 grid around the cell
                for o in range(3):  # Loop through the 3x3 grid around the cell
                    try:
                        # Check the cell in the 3x3 grid
                        if world[p - 1 + n][m - 1 + o] == "x" and p-1+n >= 0 and m-1+o >= 0:  # If the cell is alive
                            live_cell += 1  # Increment the live cell counter
                    except IndexError:
                        continue  # Skip cells outside the grid boundaries

            if world[p][m] == "x":  # If the current cell is alive
                live_cell -= 1  # Remove the current cell from the count
                if live_cell < 2:  # Underpopulation
                    new_row.append(" ")  # Cell dies
                elif live_cell < 4:  # Lives to the next generation
                    new_row.append("x")  # Cell stays alive
                else:  # Overpopulation
                    new_row.append(" ")  # Cell dies
            else:  # If the current cell is dead
                if live_cell == 3:  # Reproduction
                    new_row.append("x")  # Cell becomes alive
                else:
                    new_row.append(" ")  # Cell stays dead
        new_world.append(new_row)  # Add the new row to the new world
    return new_world  # Return the new generation grid


#
# Main program
#

# Initialize work and tmp:
try:
    # Ask user for the grid side length, default is 20
    side_length = float(input("Grid sidelength (default 20): "))
    if side_length.is_integer():  # Check if the input is an integer
        SIZE = int(side_length)  # Set the SIZE to the user input
except ValueError:
    pass  # Ignore invalid input and use default SIZE

# Ask user for the number of generations to compute
generation = 0  # Initialize the generation counter
generation_stop = False  # Flag to control the input loop
while not generation_stop:  # Loop until valid input is provided
    try:
        generation = float(input("Max generation: "))  # Ask for max generations
        if generation.is_integer():  # Check if the input is an integer
            generation = int(generation)  # Set generation to user input
            generation_stop = True  # Exit the loop
        else:
            generation_stop = False  # Continue the loop
    except ValueError:
        continue  # Ignore invalid input and ask again

# Initialize the initial configuration of the grid
work = [[" "] + ["x"] + [" "] * 18, [" "] + ["x"] + [" "] * 18, [" "] + ["x"] + [" "] * 18, [" "] * 20, [" "] * 20,
        [" "] * 20, [" "] * 20, [" "] * 20, [" "] * 20, [" "] * 20, [" "] * 10 + ["x"] * 3 + [" "] * 7,
        [" "] * 10 + ["x"] * 1 + [" "] * 9, [" "] * 10 + ["x"] * 3 + [" "] * 7, [" "] * 20, [" "] * 20, [" "] * 20,
        [" "] * 20, [" "] * 20, [" "] * 20, [" "] * 20]

# Ensure the grid size matches the specified SIZE
for i in range(20):  # Loop through the first 20 rows
    work[i] = work[i] + [" "] * (SIZE - 20)  # Extend the row to match SIZE

for j in range(SIZE - 20):  # Loop to add additional rows if SIZE > 20
    work.append([" "] * SIZE)  # Add a new row with SIZE columns

# Setup turtle window width
turtle_width = 800
# Setup turtle window height
turtle_height = 800

# Set Turtle window
turtle.setup(turtle_width, turtle_height)
# Set Turtle tracer
turtle.tracer(1)
# Set Turtle window
window = turtle.Screen()
# Set window title
window.title("Cellular Automaton")
# Create new turtle object
t = turtle.Turtle()
# Set turtle speed
t.speed(10)

def drawWork(turtle, work):
    """
    draw GUI using work list and turtle
    :param turtle: turtle object
    :param work: 2d list
    :return: Nothing
    """
    turtle.clear()  # Clear previous turtle
    rows = len(work[0])  # Get how many cells in work list
    x = turtle_width / (rows + 1)  # Calculate one block's width
    y = turtle_height / (rows + 1)  # Calculate one block's height
    turtle.penup()  # turtle penup
    for i in range(len(work)):  # For loop for draw every lines
        for j in range(len(work[i])):  # For loop for draw every cell
            if work[i][j] == "x":  # if cell is live, draw dot
                turtle.setposition((i+1)*x-400, 400-(j+1)*y)  # Move to position
                turtle.dot(5, 'black')  # Draw dot on live cell


compute = 0  # Initialize the compute counter
# Compute and display each generation until the specified generation limit
while compute <= generation:  # Loop until the max generation is reached
    drawWork(t, work)
    work = next_generation(work)  # Calculate the next generation
    time.sleep(1)  # Wait for 1 second before the next generation
    compute += 1  # Increment the generation counter
