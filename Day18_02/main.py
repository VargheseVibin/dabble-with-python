from turtle import Turtle, Screen
import random


colors = [ "blue", "wheat", "salmon", "green yellow", "dark cyan", "ForestGreen",
           "red", "rosy brown", "dark green", "deep sky blue", "crimson", "navy",]

tim = Turtle()

def draw_shape(n_sides):
    for _ in range(n_sides):
        tim.forward(100)
        tim.right(360/n)


tim.clear()
tim.pendown()

tim.home()
for n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(n)

screen = Screen()
screen.exitonclick()