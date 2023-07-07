from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.score = 1
        self.goto(-250, 250)
        self.speed("fastest")
        self.update_score()

    def update_score(self):
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def scores(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over", align="center", font=FONT)