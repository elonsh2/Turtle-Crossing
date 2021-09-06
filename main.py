import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)
car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    car_manager.create_car()
    car_manager.move_car()
    time.sleep(0.01)
    screen.update()
    # Detect car collision
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    # Detect finish
    if player.check_finish():
        scoreboard.level_up()
        time.sleep(0.5)
        car_manager.speed_up()

screen.exitonclick()
