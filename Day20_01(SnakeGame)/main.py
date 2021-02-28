from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

def draw_border():
    border = Turtle()
    border.hideturtle()
    border.color("white")
    border.penup()
    border.goto(-280, 280)
    border.pendown()
    border.goto(280, 280)
    border.goto(280, -280)
    border.goto(-280, -280)
    border.goto(-280, 280)


snake = Snake()
food = Food()
scoreboard = ScoreBoard()
draw_border()

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

    # Detect collision with Food
    if snake.head.distance(food) <= 15:
        food.refresh()
        scoreboard.increase_score()
        snake.eats_food()

    # Detect collision with wall
    if snake.detect_wall_collision():
        game_on = False
        scoreboard.game_over()
        print("Oops.. Sorry! Game Over!")

    # Detect collision with tail
    for block in snake.blocks[1:]:
        if snake.head.distance(block) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
