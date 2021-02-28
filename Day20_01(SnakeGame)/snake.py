from turtle import Turtle
STARTING_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
BLOCK_SIZE = 20
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.blocks = []
        for coordinate in STARTING_COORDINATES:
            self.make_block(coordinate)
        self.head = self.blocks[0]

    def make_block(self, coordinate):
        block = Turtle(shape="square")
        block.penup()
        block.color("white")
        block.setposition(coordinate)
        self.blocks.append(block)

    def detect_wall_collision(self):
        if pow(self.head.xcor(), 2) >= 280 * 280:
            self.head.setx(self.head.xcor() * -1)
            return True
        if pow(self.head.ycor(), 2) >= 280 * 280:
            self.head.sety(self.head.ycor() * -1)
            return True

    def move(self):
        for n in range(len(self.blocks) - 1, -1, -1):
            if n == 0:
                self.blocks[n].forward(MOVE_DISTANCE)
            else:
                self.blocks[n].setpos(self.blocks[n - 1].pos())

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def eats_food(self):
        self.make_block(self.blocks[-1].position())

    def get_snake_direction(self):
        return self.head.heading()
