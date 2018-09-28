from math import sqrt
# This gives us a function, sqrt, that square roots a number.


def quadratic_plus(a, b, c):
	# TODO: Write a function that finds one of the solutions
	# (the plus sqrt solution) to a quadratic equation in standard form.
	d = b**2 - 4*a*c
	numerator = -b + sqrt(d)
	denominator = 2*a
	return numerator / denominator
	return (-b + sqrt(b**2 - 4*a*c)) / (2 * a)


# Tests for quadratic_plus go here

# TODO: Write tests for sqrt.
x = 4
y = 9
z = 12
w = sqrt(x)
assert w == 2
assert sqrt(4) == 2
v = sqrt(y)
assert v == 3
u = sqrt(z)
assert u > 3
assert u < 4

# TODO: Write tests for quadratic_plus.
a, b, c = 1, -1, -6
d = quadratic_plus(a, b, c)
assert d == 3