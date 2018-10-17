""" 2018-10-16
Warmup: Write a function called `first_square_above` that takes one argument, `threshold`, and returns the first perfect square greater than `threshold`.

Hints: Use a `while` loop, which terminates when your perfect square is larger than `threshold`.
"""

def first_square_above(threshold):
	base = 1
	perfect_square = base**2
	# Figure out the first `perfect_square` > `threshold`
	return perfect_square

assert first_square_above(10) == 16
assert first_square_above(100) == 121

"""
Reminders:
Don't forget colons at the end of your `while` conditions and function definitions.
You can make a variable count up using `myvariable += 1`.
To square a number, use the ** operator, e.g.: `perfect_square = base ** 2`.
Oh and all those back-ticks (`) are just ways of saying "this stuff in here is a piece of code."
"""

"""
Installing pip for Python 3:
`python3 -m easy_install pip`
Or possibly:
`sudo python3 -m easy_install pip`

Confirm with:
`pip3 --version`
Should print something like:
`pip 18.1 from /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pip (python 3.7)`
"""