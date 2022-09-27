from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)
        self.timer = 0.1

    def go_up(self):
        self.forward(MOVE_DISTANCE)
    def go_left(self):

        if self.heading() != RIGHT or self.heading() ==:
            self.head.setheading(LEFT)

        def right(self):
            if self.head.heading() != LEFT:
                self.head.setheading(RIGHT)

    def reset_position(self):
        self.goto(STARTING_POSITION)
        self.timer *= 0.9