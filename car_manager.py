from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def generate_car(self):
        if randint(1, 6) == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(choice(COLORS))
            car.penup()
            car.goto(300, randint(-240, 240))
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            if car.xcor() >= -300:
                car.backward(STARTING_MOVE_DISTANCE)
            else:
                car.hideturtle()

    def increase_car_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
