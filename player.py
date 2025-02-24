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
        self.color("black")
        self.setheading(90)
        self.setup()

    def setup(self):
        self.goto(STARTING_POSITION)

    def go_forward(self):
        self.forward(MOVE_DISTANCE)

    def has_crossed_road(self):
        return self.ycor() >= FINISH_LINE_Y
