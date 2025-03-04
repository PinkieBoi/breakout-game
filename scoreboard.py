from time import sleep
from turtle import Turtle

from vboxapi import xrange


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.game_on = True
        self.lives = 3
        self.points = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-110, -270)

    def display_score(self):
        self.clear()
        self.write(f"Lives: {self.lives}\t\t\tScore: {self.points}", font=("Ubuntu", 10, "normal"))

    def hit_block(self):
        self.points += 10

    def lose_life(self):
        self.lives -= 1
        if self.lives == 0:
            self.game_on = False

    def create_countdown(self):
        self.goto(0, 0)
        for _ in xrange(5, 0, -1):
            self.clear()
            self.write(str(_), font=("Ubuntu", 15, "bold"))
            sleep(1)
        self.goto(-110, -270)
