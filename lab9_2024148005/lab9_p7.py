# Bouncing Balls Simulation Program

import turtle
import random
import time


def atLeftEdge(ball, screen_width):
    """
    Check if the ball is at the left edge of the screen
    :param ball: ball turtle object
    :param screen_width: int value
    :return: Boolean
    """
    if ball.xcor() < -screen_width / 2:
        return True
    else:
        return False


def atRightEdge(ball, screen_width):
    """
    Check if the ball is at the right edge of the screen
    :param ball: ball turtle object
    :param screen_width: int value
    :return: Boolean
    """
    if ball.xcor() > screen_width / 2:
        return True
    else:
        return False


def atTopEdge(ball, screen_height):
    """
    Check if the ball is at the top edge of the screen
    :param ball: ball turtle object
    :param screen_height: int value
    :return: Boolean
    """
    if ball.ycor() > screen_height / 2:
        return True
    else:
        return False


def atBottomEdge(ball, screen_height):
    """
    Check if the ball is at the bottom edge of the screen
    :param ball: ball turtle object
    :param screen_height: int value
    :return: Boolean
    """
    if ball.ycor() < -screen_height / 2:
        return True
    else:
        return False


def bounceBall(ball, new_direction):
    """
    Change the ball direction when ball is bouncing
    :param ball: ball turtle object
    :param new_direction: left or right or up or down
    :return:
    """
    if new_direction == 'left' or new_direction == 'right':
        new_heading = 180 - ball.heading()
    elif new_direction == 'down' or new_direction == 'up':
        new_heading = 360 - ball.heading()

    return new_heading


def createBalls(num_balls):
    """
    Create a random ball turtle object
    :param num_balls: int value
    :return: ball objects
    """
    balls = []
    for k in range(0, num_balls):
        new_ball = turtle.Turtle()
        new_ball.shape('circle')
        new_ball.fillcolor('black')
        new_ball.speed(0)
        new_ball.pendown()
        new_ball.pencolor('black')
        new_ball.setheading(random.randint(1, 359))
        balls.append(new_ball)

    return balls


# ---- main
# program greeting
print('This program simulates bouncing balls in a turtle screen')
print('for a specified number of seconds.')

# init screen size
screen_width = 800
screen_height = 600
turtle.setup(screen_width, screen_height)

# create turtle window
window = turtle.Screen()
window.title('Bouncing Balls')

# prompt user for execution time and number of balls
num_seconds = int(input('Enter number of seconds to run: '))
num_balls = int(input('Enter number of balls in simulation: '))

# create balls
balls = createBalls(num_balls)

# set start time
start_time = time.time()

# begin simulation
terminate = False

colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]


def changeColor(ball):
    while True:  # Change ball's color to random color
        color = random.choice(colors)
        if ball.color()[0] != color:
            ball.color(color)
            break


while not terminate:
    # Handle all balls
    for k in range(0, len(balls)):
        balls[k].forward(15)
        # if ball at left edge, change the direction and change color to random color
        if atLeftEdge(balls[k], screen_width):
            balls[k].setheading(bounceBall(balls[k], 'right'))
            changeColor(balls[k])
        # if ball at left edge, change the direction and change color to random color
        elif atRightEdge(balls[k], screen_width):
            balls[k].setheading(bounceBall(balls[k], 'left'))
            changeColor(balls[k])
        # if ball at left edge, change the direction and change color to random color
        if atTopEdge(balls[k], screen_height):
            balls[k].setheading(bounceBall(balls[k], 'down'))
            changeColor(balls[k])
        # if ball at left edge, change the direction and change color to random color
        elif atBottomEdge(balls[k], screen_height):
            balls[k].setheading(bounceBall(balls[k], 'up'))
            changeColor(balls[k])
        if time.time() - start_time > num_seconds:
            terminate = True

# exit on close window
turtle.exitonclick()
