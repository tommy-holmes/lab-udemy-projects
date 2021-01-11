from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


def read_high_score():
    with open("data.txt") as file:
        contents = file.read()
        return contents


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(read_high_score())
        self.goto(0, 275)
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_score()

    def write_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
