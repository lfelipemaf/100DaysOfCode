from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.pu()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(0, 250)
        self.speed("fastest")
        self.update_score()

    def update_score(self):
        self.write(f"{self.l_score}         {self.r_score}", align="center", font=("Courier", 45, "bold"))

    def r_scores(self):
        self.clear()
        self.r_score += 1
        self.update_score()

    def l_scores(self):
        self.clear()
        self.l_score += 1
        self.update_score()