from random import randint
from turtle import Turtle

t = Turtle()

# `abs` is the absolute value function.
# `t.xcor()` and `t.ycor()` get the respective coordinates of the turtle.
# The turtle starts at (0, 0).

color = 'red'
t.pencolor(color)

while not (abs(t.xcor()) > 500 or abs(t.ycor()) > 500):
	turn = randint(-44, 45)
	distance = randint(1, 20)
	t.left(turn)
	t.forward(distance)
	if color == 'red':
		color = 'green'
	else:
		color = 'red'
	t.pencolor(color)

input("<Hit ENTER to quit>")

# What will this program do when we run it?