from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colours = ['red', 'green', 'blue', 'orange', 'yellow', 'purple']
names = ['tim', 'tom', 'dick', 'harry', 'jeff', 'sam']
y_pos = -150
colour_index = 0
turtles = []

for name in names:
    name = Turtle(shape="turtle")
    name.color(colours[colour_index])
    name.penup()
    name.goto(-200, y_pos)
    turtles.append(name)
    y_pos += 50
    colour_index += 1

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            if user_bet == turtle.pencolor():
                print(f"You've won! The winning colour was {turtle.pencolor()}.")
            else:
                print(f"You've lost! The winning colour was {turtle.pencolor()}.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
