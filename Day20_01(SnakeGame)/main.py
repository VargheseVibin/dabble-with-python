import turtle as t
from turtle import Screen, Turtle
import random
import time
from snake import Snake

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake()

screen.listen()
screen.onkeypress(fun=snake.move_up,     key="Up")
screen.onkeypress(fun=snake.move_down,   key="Down")
screen.onkeypress(fun=snake.move_right,  key="Right")
screen.onkeypress(fun=snake.move_left,   key="Left")


game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    snake.move()









screen.exitonclick()