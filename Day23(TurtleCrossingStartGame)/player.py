from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setposition(x=0, y=-280)
        self.setheading(90)
        self.shape("turtle")
        self.color("black")

    def move_up(self):
        self.forward(10)
