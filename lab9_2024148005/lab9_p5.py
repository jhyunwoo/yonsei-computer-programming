#
# Please save this program to the hard-drive of your computer and set
# it up as a PyCharm project.
#

import turtle

def square(t, length):
    """
    Draw a square
    :param t: turtle object
    :param length: int value
    :return: Nothing
    """
    for s in range(4):
        t.forward(length)
        t.left(90)

def writeText():
    """
    Writes text about turtle coordination on the screen
    :return: Nothing
    """
    cord.clear()  # Clear previous text
    cord.write(f"({int(t.xcor())}, {int(t.ycor())})")  # Write coordination of turtle


def closeDown():
    """
    Close the window
    :return: Nothing
    """
    turtle.bye()

def drawShape(x, y):
    """
    Draws a shape on the screen
    :param x: x coordinate
    :param y: y coordinate
    :return: Nothing
    """
    t.penup()
    t.setpos(x, y)
    t.pendown()
    t.begin_fill()
    if x <= 100: #Left third:
        t.color("green")
        square(t, 10)
    elif 100 < x <= 200: #Middle third:
        t.color("red")
        t.circle(10)
    else:
        t.color("blue")
        square(t, 10)
    t.end_fill()

#
# main:
#

# Set window to be 300 x 200 with the point (0, 0) as the lower-left
# corner and (300, 200) as the upper right corner:
turtle.setup(300, 200)
turtle.screensize(300, 200)
turtle.setworldcoordinates(0, 0, 300, 200)

# Initialize global turtle t variable which will be used inside
# of the handler functions:
t = turtle.getturtle()
t.speed(0) # Set fastest screen update speed for this turtle.

# Initialize global turtle cord which will be use inside of the handler functions
cord = turtle.Turtle()
cord.setposition(0,0)

# Draw two vertical lines to divide the window into thirds:
t.penup()
t.setpos(100, 0) #First line
t.pendown()
t.setpos(100, 200)
t.penup()
t.setpos(200, 0) #Second line
t.pendown()
t.setpos(200, 200)


# Register callback for key-press events:
turtle.onkey(writeText, 'Up')
turtle.onkey(closeDown, 'q')
# Register callback for mouse on-click events:
turtle.onscreenclick(drawShape)
# Enter event loop:
turtle.listen()
turtle.mainloop()
