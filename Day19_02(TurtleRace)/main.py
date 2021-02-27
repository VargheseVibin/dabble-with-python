import turtle as t
from turtle import Screen
import random

colors =["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()
screen.setup(width=500, height=400)
your_bet = screen.textinput(title="Make your bet", prompt="Which turtle are you betting on to win the race? Enter a color:")

turtles = []
x = -240
y = -100
gap = 0

for color in colors:
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x, y+gap)
    gap += 30
    new_turtle.speed(7)
    turtles.append(new_turtle)

race_on = True
while race_on:
    for turtle in turtles:
        if turtle.xcor() >= 240:
            race_on = False
            winner_color = turtle.pencolor()
            if your_bet == winner_color:
                print(f"Yay!! You've won the bet... {winner_color} is the winner of the race")
            else:
                print(f"Oops!! You've lost the bet... {winner_color} is the winner of the race")
        turtle.forward(random.randint(0, 10))


screen.exitonclick()
