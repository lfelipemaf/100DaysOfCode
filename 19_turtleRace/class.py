from turtle import Turtle, Screen

tim = Turtle(shape="turtle")
screen = Screen()


def f():
    tim.fd(10)

def d():
    tim.bk(10)

def l():
    tim.left(10)

def r():
    tim.right(10)


screen.onkey(f, "w")
screen.onkey(d, "s")
screen.onkey(l, "a")
screen.onkey(r, "d")

screen.listen()
screen.exitonclick()
