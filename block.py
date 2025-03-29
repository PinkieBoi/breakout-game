from random import choice
from turtle import Turtle


class Block(Turtle):

    def __init__(self, name):
        super().__init__()
        self.penup()
        self.name = name
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(choice(["red", "yellow", "orange", "pink", "green"]))
