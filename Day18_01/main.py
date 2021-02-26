from turtle import Turtle, Screen
import random


tim = Turtle()
for _ in range(4):
    tim.forward(100)
    tim.left(90)

tim.clear()

for _ in range(15):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)


screen = Screen()
screen.exitonclick()

