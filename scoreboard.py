from turtle import Turtle


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
