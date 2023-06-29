from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    """Move the turtle forward 10 paces"""
    tim.forward(10)


move_forward()
screen.listen()
screen.onkey(key="space", fun=move_forward())
screen.exitonclick()
