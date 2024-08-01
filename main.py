import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
level = Scoreboard()
cars = CarManager()

screen.onkeypress(player.go_forward, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.generate_car()
    cars.move_cars()

    if player.has_crossed_road():
        player.setup()
        level.update_level()
        cars.increase_car_speed()

    for car in cars.cars:
        if car.distance(player) <= 20:
            game_is_on = False
