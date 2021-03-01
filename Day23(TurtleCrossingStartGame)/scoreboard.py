from turtle import Turtle

LEVEL_FONT = ("Courier", 16, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.setposition(x=-280, y=270)
        self.color("black")
        self.write(f"Level : {self.level}", move=False,align="left" , font=LEVEL_FONT)
