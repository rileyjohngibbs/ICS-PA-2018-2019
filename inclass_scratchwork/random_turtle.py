from random import randint
from turtle import Turtle

t = Turtle()

# `randint(a, b)` returns a random integer between `a` and `b`, inclusive. So `randint(1, 6)` is like rolling a six-sided die.

paths_taken = 0
# color = 'red'
# t.pencolor(color)

while not paths_taken >= 10:
	turn = randint(-179, 180)
	distance = randint(5, 100)
	t.left(turn)
	t.forward(distance)
	# if color == 'red':
	# 	color = 'green'
	# else:
	# 	color = 'red'
	# t.pencolor(color)
	paths_taken += 1

input("<Hit ENTER to quit>")

# What will this program do when we run it?