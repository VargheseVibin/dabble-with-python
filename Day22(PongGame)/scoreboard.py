from turtle import Turtle
SCORE_FONT = ("Courier", 50, "bold")
L_SCORE_LOC = (-100, 220)
R_SCORE_LOC = (100, 220)


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.show_scores()

    def show_scores(self):
        self.clear()
        self.setposition(L_SCORE_LOC)
        self.write(f"{self.l_score}", move=False, font=SCORE_FONT)
        self.setposition(R_SCORE_LOC)
        self.write(f"{self.r_score}", move=False, font=SCORE_FONT)

    def increase_r_score(self):
        self.r_score += 1
        self.show_scores()

    def increase_l_score(self):
        self.l_score += 1
        self.show_scores()
