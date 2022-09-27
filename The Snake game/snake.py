from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.all_snakes = []
        self.create_snake()
        self.head = self.all_snakes[0]

    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_segment(i)

    def add_segment(self, position):
        new_snake = Turtle("square")
        new_snake.color("beige")
        new_snake.penup()
        new_snake.goto(position)
        self.all_snakes.append(new_snake)

    def extend(self):
        self.add_segment(self.all_snakes[-1].position())

    def move(self):
        for snake_num in range(len(self.all_snakes) - 1, 0, -1):
            new_x = self.all_snakes[snake_num - 1].xcor()
            new_y = self.all_snakes[snake_num - 1].ycor()
            self.all_snakes[snake_num].goto(new_x, new_y)

        self.head.forward(MOVE_FORWARD)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
