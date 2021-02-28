from turtle import Turtle
WIDTH = 20
HEIGHT = 100
UP = 90
DOWN = 270
MOVEDISTANCE = 20

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.x_pos = 350
        self.y_pos = 0
        self.penup()
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.setposition(x=self.x_pos, y=self.y_pos)

    def move_up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + MOVEDISTANCE)

    def move_down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - MOVEDISTANCE)


