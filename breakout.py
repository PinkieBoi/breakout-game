from time import sleep
from scoreboard import Scoreboard
from turtle import *
from platform_paddle import Platform
from ball import Ball


win = Screen()
win.setup(600, 600)
win.bgcolor("black")
win.title("BreakOut")
win.tracer(0)
win.listen()

scoreboard = Scoreboard()
platform = Platform()
ball = Ball("normal")

win.onkeypress(platform.move_right, "Right")
win.onkeypress(platform.move_left, "Left")

while scoreboard.game_on:
    win.update()
    sleep(0.001)
    scoreboard.display_score()
    ball.move_ball()

    # Detect life lost
    if ball.ycor() <= -275:
        scoreboard.lose_life()
        ball.reset_ball()
        scoreboard.create_countdown()

    # Detect paddle bounce
    ball.platform_bounce(platform)


win.mainloop()
