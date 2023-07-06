from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.pu()
        self.hideturtle()
        self.speed("fastest")

    def write_state(self, x, y, state_name):
        self.goto(x, y)
        self.write(f"{state_name}", align="center", font=("Arial", 8, "normal"))

