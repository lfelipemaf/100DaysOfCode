from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def f():
    tim.fd(50)
    tim.lt(60)

screen.onkey(f, "space")
screen.listen()
screen.exitonclick()
