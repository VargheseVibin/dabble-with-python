from turtle import Turtle

LEVEL_FONT = ("Courier", 16, "normal")
GAME_OVER_FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.show_level()

    def show_level(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.setposition(x=-280, y=270)
        self.color("black")
        self.write(f"Level : {self.level}", move=False, align="left", font=LEVEL_FONT)

    def game_over(self):
        self.penup()
        self.hideturtle()
        self.setposition(x=0, y=0)
        self.color("black")
        self.write(f"Sorry..Game Over!", move=False, align="center", font=LEVEL_FONT)

    def upgrade_level(self):
        self.level += 1
        self.show_level()

