from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            new_car.penup()
            random_y = randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.move_distance)

    def is_collided(self, player):
        collided = 0
        for car in self.all_cars:
            if car.distance(player) < 20:
                print("crashed")
                collided = 1
                break
        if collided == 1:
            return True
        else:
            return False

    def level_up(self):
        self.move_distance += MOVE_INCREMENT
