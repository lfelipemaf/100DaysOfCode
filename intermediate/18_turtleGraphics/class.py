import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()

tim.shape("circle")
tim.color("black", "LimeGreen")
# # Challenge 1 - Draw a Square
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)
#
# # DChallenge 2 - Draw a Dashed Line
# for _ in range(15):
#     tim.fd(10)
#     tim.pu()
#     tim.fd(10)
#     tim.pd()
#
# # Challenge 3 - Drawing Different Shapes
#


# for a in range(3, 11):
#     angle = 360 / a
#     tim.pencolor(random.choice(colors))
#     for i in range(a):
#
#         tim.forward(100)
#         tim.right(angle)

# # Challenge 4 - Generate a Random Walk
turtle.colormode(255)
# direction = [0, 90, 180, 270]
# tim.pensize(10)
tim.speed('fastest')


#
def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue


# for i in range(200):
#     tim.pencolor(random_color())
#     tim.color(random_color())
#     tim.fd(30)
#     tim.right(random.choice(direction))

# Challenge 5 - Draw a Spirograph

for i in range(200):
    tim.pencolor(random_color())
    tim.circle(200)
    current_heading = tim.heading()
    tim.setheading(current_heading + 10)

screen = Screen()
screen.exitonclick()
