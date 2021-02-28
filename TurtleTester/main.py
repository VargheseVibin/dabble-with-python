from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()
tim.shape("square")
tim.shapesize(stretch_len=1, stretch_wid=5)
tim.forward(50)

screen.exitonclick()