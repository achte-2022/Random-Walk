#Importing Libraries
import turtle
import random

#Constants
MAX_INTENSITY = 255
ANGLES = [0, 90, 180, 270]
WALK_LENGTH = 25
NUM_WALKS = 200
SHAPE = 'classic'
SPEED = 'fastest'
WIDTH = 7
BG_COLOR = 'black'


#Color Setup
turtle.colormode(MAX_INTENSITY)

#Generate Random Color
def random_color():
    red = random.randint(0, MAX_INTENSITY)
    green = random.randint(0, MAX_INTENSITY)
    blue = random.randint(0, MAX_INTENSITY)
    return (red, green, blue)

#Random Walk Algorithm
def random_walk(turtle_object, num_walks, walk_length):
    for _ in range(num_walks):
        angle = random.choice(ANGLES)
        color = random_color()
        turtle_object.color(color)
        turtle_object.right(angle)
        turtle_object.forward(walk_length)
    return

#Object Setup
window = turtle.Screen()
window.bgcolor(BG_COLOR)
turtle_object = turtle.Turtle()
turtle_object.shape(SHAPE)
turtle_object.width(WIDTH)
turtle_object.speed(SPEED)

random_walk(turtle_object, NUM_WALKS, WALK_LENGTH)
turtle_object.hideturtle()

window.exitonclick()
