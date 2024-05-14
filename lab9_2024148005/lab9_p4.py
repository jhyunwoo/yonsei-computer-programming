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