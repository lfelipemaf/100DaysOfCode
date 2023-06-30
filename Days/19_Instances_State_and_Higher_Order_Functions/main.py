from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Turtle Race", "Which turtle will win the race?\n - Red\n - Orange\n - Yellow\n - "
                                           "Green\n - Blue\n - Purple\n - Pink").lower()
red_turtle = Turtle(shape="turtle")
red_turtle.color("red")
red_turtle.pu()
red_turtle.goto(x=-240, y=100)
blue_turtle = Turtle(shape="turtle")
blue_turtle.color("blue")
blue_turtle.pu()
blue_turtle.goto(x=-240, y=70)

screen.exitonclick()
