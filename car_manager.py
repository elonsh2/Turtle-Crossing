from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 1
MOVE_INCREMENT = 1


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.spawn_chance_max = 27

    def create_car(self):
        spawn_chance = randint(0, self.spawn_chance_max)
        if spawn_chance == 0:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            new_car.goto(x=300, y=randint(-250, 250))
            new_car.right(180)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
        self.spawn_chance_max -= 1

    def reset(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        self.spawn_chance_max = 27
