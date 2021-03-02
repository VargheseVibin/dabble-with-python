from turtle import Turtle

SCOREFONT = ("Courier", 10, "bold")
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score(self)
        self.penup()
        self.hideturtle()
        self.setposition(x=0, y=280)
        self.color("white")
        self.set_score()

    def set_score(self):
        self.write(f"Snake Score:{self.score} ; High Score:{self.high_score}",
                   move=False, align="center", font=SCOREFONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.set_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.color("red")
        self.write(f"GAME OVER!", move=False, align="center", font=SCOREFONT)
        if self.score > self.high_score:
            self.update_high_score()

    @staticmethod
    def get_high_score(self):
        with open(file="data.txt", mode="r") as score_file:
            h_score = int(score_file.read())
            return h_score

    def update_high_score(self):
        with open(file="data.txt", mode="w") as score_file:
            score_file.write(str(self.score))
