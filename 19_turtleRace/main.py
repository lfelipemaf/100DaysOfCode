from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Turtle Race", "Which turtle wil win?")
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "black"]
y_position = [ -90, -60, -30, 0, 30, 60, 90, 120]
turtles = []



if user_bet:
    is_race_on = True

for turtle in range(0, 8):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle])
    new_turtle.pu()
    new_turtle.goto(x=-240, y=y_position[turtle])
    turtles.append(new_turtle)

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print("You won!")
            else:
                print(f"You lose, the winner was {winning_turtle}")
            is_race_on = False
        distance = random.randint(0, 10)
        turtle.forward(distance)






screen.exitonclick()