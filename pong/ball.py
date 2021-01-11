from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.delta_x = 10
        self.delta_y = 10
        self.movement_speed = .1

    def move(self):
        new_x = self.xcor() + self.delta_x
        new_y = self.ycor() + self.delta_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.delta_y *= -1

    def bounce_x(self):
        self.delta_x *= -1
        self.movement_speed *= .9

    def restart(self):
        self.goto(0, 0)
        self.bounce_x()
        self.movement_speed = .1
