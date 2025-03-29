from random import randint
from turtle import Turtle


class Ball(Turtle):

    def __init__(self, difficulty):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.speed(6)
        self.goto(0, -210)
        self.seth(randint(15, 166))
        if self.heading() == 90:
            self.seth(randint(10, 170))
        if difficulty == "hard":
            self.speed(0)
        elif difficulty == "easy":
            self.speed(3)
        else:
            self.speed(5)

    def wall_bounce(self):
        if self.xcor() >= 270 or self.xcor() <= -270:
            if self.heading() in range(91, 180) or self.heading() in range(271, 360):
                self.rt(randint(80, 120))
                self.fd(20)
            else:
                self.lt(randint(80, 120))
                self.fd(20)

    def roof_bounce(self):
        if self.ycor() >= 280:
            if self.heading() in range(91, 180):
                self.lt(randint(80, 120))
                while self.heading() < 182:
                    self.lt(10)
                self.fd(1)
            else:
                self.rt(randint(80, 120))
                self.fd(1)

    def move_ball(self, blocks):
        self.fd(1)
        self.wall_bounce()
        self.roof_bounce()
        self.block_bounce(blocks)

    def platform_bounce(self, platform):
        if self.ycor() < -210:
            if platform.xcor() - 40 <= self.xcor() <= platform.xcor() + 40:
                if self.heading() > 270:
                    self.lt(randint(80, 120))
                else:
                    self.rt(randint(80, 120))
                self.fd(10)

    # TODO: Make this work
    def block_bounce(self, blocks_remaining):
        for block in blocks_remaining:
            if self.ycor() - 5 <= block.ycor() <= self.ycor() + 5:
                if self.xcor() - 20 <= block.xcor() <= block.xcor() + 20:
                    if self.heading() in range(91, 180) or self.heading() in range(271, 360):
                        self.rt(100)
                        self.fd(10)
                    else:
                        self.lt(100)
                        self.fd(10)

    def reset_ball(self):
        self.goto(0, -210)
        self.seth(randint(15, 166))
        if self.heading() == 90:
            self.seth(randint(10, 170))

