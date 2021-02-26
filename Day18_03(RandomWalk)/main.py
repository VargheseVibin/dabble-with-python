from turtle import Screen
import turtle as t
import random

turn_angles = [0, 90, 180, 270]
colors = [ "blue", "wheat", "salmon", "green yellow", "dark cyan", "ForestGreen",
           "red", "rosy brown", "dark green", "deep sky blue", "crimson", "navy",]
t.colormode(255)
tim = t.Turtle()
tim.width(10)
# tim.speed(10)
tim.speed("fastest")


def gen_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


for _ in range(200):
    tim.setheading(random.choice(turn_angles))
    tim.pencolor(gen_random_color())
    tim.forward(20)


screen = Screen()
screen.exitonclick()