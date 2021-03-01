from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(360, 0)
l_paddle = Paddle(-360, 0)
ball = Ball()
scoreboard = ScoreBoard()

# screen.update()
screen.listen()
screen.onkeypress(fun=r_paddle.move_up, key="Up")
screen.onkeypress(fun=r_paddle.move_down, key="Down")
screen.onkeypress(fun=l_paddle.move_up, key="w")
screen.onkeypress(fun=l_paddle.move_down, key="s")

game_on = True

while game_on:
    time.sleep(ball.ball_move_speed)
    screen.update()
    ball.move_ball()

    # Detect Collision of ball with Horizontal Wall
    ball.detect_horizontal_wall_collision()

    # Detect Collision of paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.detect_paddle_collision()

    # Detect Right Paddle Miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_l_score()

    # Detect Left Paddle Miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_r_score()


screen.exitonclick()
