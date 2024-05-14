def drawCoordinates(myturtle, coordList, d):
    """ Draw a line between coordinate points on the screen.
    coordList contains a tuple of sub-tuples. Each
    sub-tuple contains an integer x, integer y, and a
    Boolean. The x,y pair represents a coordinate in the
    window, and the Boolean indicates whether the pen is
    used. At each point, a circle with diameter d should
    also be drawn. The first line of each consecutive line
    drawing should be colored blue.
    """
    for coord in coordList:  # Draw all coord in coordList
        if coordList.index(coord) > 0:  # if is not first coord
            # Check it consecutively follows another line
            if (coord[2] and not coordList[coordList.index(coord) - 1][2]) or (
                    not coord[2] and coordList[coordList.index(coord) - 1][2]):
                myturtle.color('blue')
            else:
                myturtle.color('black')
        else:
            myturtle.color('blue')

        # Control pen up and down using coord third value
        if coord[2]:
            myturtle.pendown()
        else:
            myturtle.penup()

        # Move to coord
        myturtle.setposition(coord[0], coord[1])
        # Draw circle that radius is d
        myturtle.dot(d)


# Test Code
import turtle

coordList = ((-350, 80, False), (-210, 80, True), (-280, 80, False),
             (-280, -60, True), (-40, 80, False), (-180, 80, True),
             (-180, -60, True), (-40, -60, True), (-180, 10, False),
             (-40, 10, True), (130, 80, False), (-10, 80, True),
             (-10, 10, True), (130, 10, True), (130, -60, True),
             (-10, -60, True), (160, 80, False), (300, 80, True),
             (230, 80, False), (230, -60, True))
# set window size:
turtle.setup(800, 200)
# get reference to turtle window:
window = turtle.Screen()
turtle.hideturtle()
drawCoordinates(turtle, coordList, 8)

window.exitonclick()
