# *args collect params into a tuple.
def add(*args):
    sum_nos = 0
    for n in args:
        sum_nos += n
    print(f"Sum of numbers:{sum_nos}")


add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def calculate(n, **kwargs):
    print(kwargs)
    print(kwargs["add"])
    print((kwargs["multiply"]))
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(f"Result of add and multiple is {n}")


calculate(23, add=4, multiply=8)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.year = kwargs.get("year")


my_car = Car(make="Volkswagen", model="Golf", color="Black")
print(my_car.model)
print(my_car.make)
print(my_car.color)
print(my_car.year)
