from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')

right_paddle = Paddle(y_position=350)
left_paddle = Paddle(y_position=-350)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.move_up, 'Up')
screen.onkey(right_paddle.move_down, 'Down')
screen.onkey(left_paddle.move_up, 'w')
screen.onkey(left_paddle.move_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.movement_speed)
    ball.move()
    screen.update()

    # Ball collides with top/bottom:
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    # Ball collides with paddle:
    if right_paddle.distance(ball) < 50 and ball.xcor() > 320 or left_paddle.distance(ball) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Ball misses right paddle and hits wall:
    if ball.xcor() > 340:
        scoreboard.add_to_left()
        ball.restart()

    # Ball misses left paddle and hits wall:
    if ball.xcor() < -340:
        scoreboard.add_to_right()
        ball.restart()


screen.exitonclick()