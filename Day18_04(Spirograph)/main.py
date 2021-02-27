import turtle as t
from turtle import Screen
import  random

t.colormode(255)
tim = t.Turtle()
# tim.circle(100)


def gen_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


tim.speed("fastest")


def draw_spirograph(gap_angle):
    for n in range(int(360/gap_angle)):
        tim.right(gap_angle)
        tim.color(gen_random_color())
        tim.circle(100)


draw_spirograph(3)

screen = Screen()
screen.exitonclick()