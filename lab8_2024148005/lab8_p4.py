#
# This program draw x on window using turtle object in Python
#

# import turtle from python default library
import turtle

# Set window size
turtle.setup(800, 600)

# Show screen
window = turtle.Screen()
# Set window's title
window.title('Draw X on window')
# Get turtle for drawing lines
the_turtle = turtle.getturtle()
# Hide turtle
the_turtle.hideturtle()
# Pen up for drawing unnecessary lines
the_turtle.penup()
# Move to top left corner
the_turtle.setposition(-400, 300)
# Pen down for drawing line
the_turtle.pendown()
# Move to bottom right corner
the_turtle.setposition(400, -300)
# Pen up for drawing unnecessary lines
the_turtle.penup()
# Move to bottom left corner
the_turtle.setposition(-400, -300)
# Pen down for drawing line
the_turtle.pendown()
# Move to top right corner
the_turtle.setposition(400, 300)
# Do not close window until user click window
window.exitonclick()
