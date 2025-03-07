# TODO: Implement bouncing using real physics.

from turtle import Turtle
from random import randint


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.speed(6)
        self.goto(0, -210)
        self.seth(randint(15, 166))
        if self.heading() == 90:
            self.seth(randint(10, 170))

    def wall_bounce(self):
        # randomizer to avoid always bouncing at 90 degrees
        bounce_angle = randint(80, 100)
        if self.xcor() >= 270 or self.xcor() <= -270:
            if self.heading() in range(91, 180) or self.heading() in range(271, 360):
                self.rt(bounce_angle)
                self.fd(20)
            else:
                self.lt(bounce_angle)
                self.fd(20)

    def roof_bounce(self):
        # randomizer to avoid always bouncing at 90 degrees
        bounce_angle = randint(80, 100)
        if self.ycor() >= 280:
            if self.heading() in range(91, 180):
                self.lt(bounce_angle)
                while self.heading() < 182:
                    self.lt(10)
                self.fd(1)
            else:
                self.rt(bounce_angle)
                self.fd(1)

    def platform_bounce(self, platform):
        # randomizer to avoid always bouncing at 90 degrees
        bounce_angle = randint(80, 100)
        if self.ycor() < -210:
            if platform.xcor() - 40 <= self.xcor() <= platform.xcor() + 40:
                if self.heading() > 270:
                    self.lt(bounce_angle)
                else:
                    self.rt(bounce_angle)
                self.fd(10)

    def break_block(self):
        # randomizer to avoid always bouncing at 90 degrees
        bounce_angle = randint(80, 100)
        if self.heading() in range(91, 180) or self.heading() in range(271, 360):
            self.rt(bounce_angle)
            self.fd(20)
        else:
            self.lt(bounce_angle)
            self.fd(20)

    def move_ball(self):
        self.fd(1)
        self.wall_bounce()
        self.roof_bounce()

    def reset_ball(self):
        self.goto(0, -210)
        self.seth(randint(15, 166))
        if self.heading() == 90:
            self.seth(randint(10, 170))
