from random import choice
from turtle import Turtle


class Block(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(choice(["red", "pink", "orange", "yellow", "blue"]))
