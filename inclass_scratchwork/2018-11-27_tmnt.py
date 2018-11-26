from random import randint
from turtle import Turtle, turtles

"""
For each subclass of Turtle, implement a unique travel method.
Leonardo has his own travel method already, but feel free to change that
    to whatever you like.
The rand_angle function is provided as a convenience. You do not have to
    use it if you don't want to.
"""


def rand_angle(n=5):
    """
    Returns a random number between -180 and 180.
    Larger values of `n` increase the tendency toward zero.
    """
    if n <= 0:
        return 0
    arc = 180/n
    return sum(randint(-arc, arc) for count in range(n))


class Leonardo(Turtle):

    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("turtle")
        self.setheading(0)
        self.up()

    def travel(self):
        self.left(rand_angle())
        self.forward(10)


class Michaelangelo(Turtle):

    def __init__(self):
        super().__init__()
        self.color("orange")
        self.shape("turtle")
        self.setheading(90)
        self.up()

    def travel(self):
        # TODO: Implement this turtle's travel pattern
        pass


class Donatello(Turtle):

    def __init__(self):
        super().__init__()
        self.color("purple")
        self.shape("turtle")
        self.setheading(180)
        self.up()

    def travel(self):
        # TODO: Implement this turtle's travel pattern
        pass


class Raphael(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("turtle")
        self.setheading(270)
        self.up()

    def travel(self):
        # TODO: Implement this turtle's travel pattern
        pass


leo = Leonardo()
mikey = Michaelangelo()
donny = Donatello()
raf = Raphael()

for x in range(30):
    for ninja in turtles():  # Loops through all of the Turtles on screen
        ninja.travel()  # Calls the travel method, which should be different for each Turtle subclass
