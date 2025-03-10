# TODO: Implement Levels
# TODO: Create blocks for level
# TODO: Detect ball / block collision

from turtle import *
from ball import Ball
from time import sleep
from scoreboard import Scoreboard
from platform_paddle import Platform


def create_pyramid():
    x = [0, 20, 40, 60, 80, 100, 120, 140]
    y = [0, 10, 20, 30, 40, 50, 60, 70]
    rows = 6
    blocks = []
    return blocks


def create_i_pyramid():
    x = [0, 20, 40, 60, 80, 100]
    y = [0, 20, 40, 60, 80, 100]
    rows = 6
    blocks = []
    return blocks


def create_columns():
    rows = 6
    blocks = []
    return blocks


def continue_game():
    pass


win = Screen()
win.setup(600, 600)
win.bgcolor("black")
win.title("BreakOut")
win.tracer(0)
win.listen()

scoreboard = Scoreboard()
platform = Platform()
ball = Ball()

win.onkeypress(platform.move_right, "Right")
win.onkeypress(platform.move_left, "Left")

def main():
    while scoreboard.game_on:
        # while scoreboard.levels < 11:
        win.update()
        sleep(0.001)
        scoreboard.display_score()
        ball.move_ball()

        # Detect life lost
        if ball.ycor() <= -275:
            scoreboard.lose_life()
            platform.reset_platform()
            ball.reset_ball()
            sleep(3)

        # Detect collision with block

        # Detect paddle bounce
        ball.platform_bounce(platform)


if __name__ == "__main__":
    main()

win.mainloop()
