from turtle import Turtle
import random

CAR_COLORS = ["red", "green", "yellow", "blue", "cyan", "orange", "purple", ]
START_X = 260
START_Y = -240

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.create_random_car()

    def spin_up_cars(self):
        for n in range(0, 13):
            x_pos = START_X
            y_pos = (START_Y+(n*40))
            new_car = self.create_car(x_pos, y_pos)
            self.cars.append(new_car)

    def create_car(self, x_pos, y_pos):
        new_car = Turtle()
        new_car.goto(x=x_pos, y=y_pos)
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(CAR_COLORS))
        new_car.setheading(180)
        return new_car

    def remove_cars_finishing_track(self):
        for car in self.cars:
            if car.xcor() < - 340:
                car.clear()
                self.cars.remove(car)

    def move_cars(self):
        for car in self.cars:
            # car.forward(random.randint(1, 10))
            car.forward(5)

    def create_random_car(self):
        x_pos = START_X
        y_pos = (START_Y + (random.randint(1, 12) * 40))
        new_car = self.create_car(x_pos, y_pos)
        self.cars.append(new_car)

