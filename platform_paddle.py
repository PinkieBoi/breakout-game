from turtle import Turtle

class Platform(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=4)
        self.goto(0, -225)

    def move_right(self):
        self.fd(10)

    def move_left(self):
        self.bk(10)

    def reset_platform(self):
        self.goto(0, -225)
