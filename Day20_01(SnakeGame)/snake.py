from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.blocks = []
        for n in range(0, 3):
            block = Turtle(shape="square")
            block.penup()
            block.color("white")
            block.setx(x=0 - (n * 20))
            block.sety(y=0)
            self.blocks.append(block)
        self.head = self.blocks[0]

    def check_and_switch_sides(self, curr_block):
        if pow(curr_block.xcor(), 2) == 300 * 300:
            curr_block.setx(curr_block.xcor() * -1)
        if pow(curr_block.ycor(), 2) == 300 * 300:
            curr_block.sety(curr_block.ycor() * -1)

    def move(self):
        for n in range(len(self.blocks) - 1, -1, -1):
            if n == 0:
                self.blocks[n].forward(MOVE_DISTANCE)
            else:
                self.blocks[n].setpos(self.blocks[n - 1].pos())
            self.check_and_switch_sides(self.blocks[n])

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.check_and_switch_sides(self.head)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.check_and_switch_sides(self.head)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.check_and_switch_sides(self.head)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.check_and_switch_sides(self.head)
