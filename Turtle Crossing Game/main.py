import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()

screen.onkeypress(player.go_up, "Up")
screen.onkeypress(player.go_left, "Left")
screen.onkeypress(player.go_right, "Right")


game_is_on = True
while game_is_on:
    time.sleep(player.timer)
    screen.update()
    car_manager.create_car()

    car_manager.move_cars()

    # collision check
    if car_manager.is_collided(player):
        score.game_over()
        break

    # Scoreboard update
    if player.ycor() > 280:
        player.reset_position()
        score.update_scoreboard()
        car_manager.level_up()

screen.exitonclick()