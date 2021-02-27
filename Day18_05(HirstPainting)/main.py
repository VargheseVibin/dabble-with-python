import colorgram
from turtle import Screen
import turtle as t
import random
# colors = colorgram.extract("hirst_dot.jpg", 20)
#
# rgb_colors=[]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)

colors = [ (237, 230, 96), (13, 115, 170),
          (166, 79, 46), (188, 12, 63), (213, 157, 87), (129, 181, 203), (234, 76, 46), (33, 139, 83), (5, 34, 91),
          (146, 167, 35), (76, 40, 21), (110, 187, 165), (167, 47, 91), (227, 117, 147), (14, 170, 212), (59, 160, 89)]



tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(350)
tim.setheading(0)
tim.hideturtle()

row_dot_count =20
col_dot_count =20
pace_count = 20

for n in range(1, (row_dot_count*col_dot_count)+1):
    tim.dot(10,random.choice(colors))
    tim.forward(pace_count)
    if n%row_dot_count == 0:
        tim.setheading(90)
        tim.forward(pace_count)
        tim.setheading(180)
        tim.forward(pace_count*row_dot_count)
        tim.setheading(0)





screen = Screen()
screen.exitonclick()
