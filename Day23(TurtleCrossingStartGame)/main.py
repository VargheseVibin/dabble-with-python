from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("white")
screen.title("Turtle Crossing Start")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkeypress(fun=player.move_up, key="Up")
scoreboard = ScoreBoard()
car_manager = CarManager()
game_on = True


i=0
while game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()
    car_manager.remove_cars_finishing_track()
    if (i%6 == 0):
        car_manager.create_random_car()
        i = 0
    i += 1
screen.exitonclick()