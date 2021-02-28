from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle = Paddle()

# screen.update()
screen.listen()
screen.onkeypress(fun=paddle.move_up, key="Up")
screen.onkeypress(fun=paddle.move_down, key="Down")

game_on = True

while game_on:
    screen.update()


screen.exitonclick()
