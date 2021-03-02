from turtle import Turtle
START_POS = (0, -280)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(START_POS)
        self.setheading(90)
        self.shape("turtle")
        self.color("black")

    def move_up(self):
        self.forward(10)

    def detect_player_route_completion(self):
        if self.ycor() >= 290:
            self.setposition(START_POS)
            return True
        else:
            return False
