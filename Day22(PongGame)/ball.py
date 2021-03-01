from turtle import Turtle
CORNER_COORDINATES = (360, 270)
TOP_WALL_YCOR = 280


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.shape("circle")
        self.color("white")
        self.penup()
        self.ball_move_speed = 0.1

    def move_ball(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(x=new_x, y=new_y)

    def detect_horizontal_wall_collision(self):
        if pow(self.ycor(), 2) >= TOP_WALL_YCOR*TOP_WALL_YCOR:
            self.y_move *= -1

    def detect_paddle_collision(self):
        self.x_move *= -1
        self.ball_move_speed *= 0.5

    def reset_position(self):
        self.setposition(x=0, y=0)
        self.x_move *= -1
        self.ball_move_speed = 0.9
