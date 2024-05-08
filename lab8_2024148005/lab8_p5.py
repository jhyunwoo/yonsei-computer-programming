import turtle


def drawSquare(myturtle: turtle, x: int, y: int, a: int):
    """
    This function draws a square based on x, y, and a values
    :param myturtle: turtle object
    :param x: x coordinate of left bottom corner of the square
    :param y: y coordinate of left bottom corner of the square
    :param a: length of the square
    :return: nothing
    """
    myturtle.penup()  # Pen up for not drawing unnecessary lines
    myturtle.setposition(x, y)  # Move to x, y coordinate
    myturtle.pendown()  # Pen down for drawing lines
    myturtle.setposition(x + a, y)  # Move to bottom right corner of the square
    myturtle.setposition(x+a, y+a)  # Move to top right corner of the square
    myturtle.setposition(x, y+a)  # Move to top left corner of the square
    myturtle.setposition(x, y)  # Move to bottom left corner of the square

