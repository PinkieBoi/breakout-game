# TODO: Implement Levels
# TODO: Detect ball / block collision
from turtle import *
from ball import Ball
from time import sleep
from block import Block
from scoreboard import Scoreboard
from platform_paddle import Platform


def create_pyramid():
    pass


def create_i_pyramid():
    pass


def create_columns():
    x_cors = [-180, -140, -20, 20, 140, 180]
    y_cors = [40, 60, 80, 100, 120, 140, 160, 180]
    all_blocks = []
    next_name = str(len(all_blocks))
    for y_position in y_cors:
        for x_position in x_cors:
            block = Block(next_name)
            block.goto(x=x_position, y=y_position)
            all_blocks.append(block)
    return all_blocks


win = Screen()
win.setup(600, 600)
win.bgcolor("black")
win.title("BreakOut")
win.tracer(0)
win.listen()


def continue_game():
    pass

countdown_timer = Turtle()
countdown_timer.hideturtle()
countdown_timer.penup()
countdown_timer.color("white")

scoreboard = Scoreboard()
platform = Platform()
ball = Ball("normal")

win.onkeypress(platform.move_right, "Right")
win.onkeypress(platform.move_left, "Left")

def main():
    game_blocks = create_columns()
    while scoreboard.game_on:
        # while scoreboard.levels < 11:
        win.update()
        sleep(0.001)
        scoreboard.display_score()
        ball.move_ball(game_blocks)

        # Detect life lost
        if ball.ycor() <= -275:
            scoreboard.lose_life()
            ball.reset_ball()
            platform.reset_platform()
            sleep(3)

        # Detect block collision & remove block


        # Detect paddle bounce
        ball.platform_bounce(platform)


if __name__ == "__main__":
    main()

win.mainloop()
