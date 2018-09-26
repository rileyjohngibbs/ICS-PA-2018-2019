def multiplicative_inverse(x):
	# Finds the multiplicative inverse of x.
	# TODO: Handle edge cases and invalid inputs.
	# If x is 0, then print a message to the user telling them they screwed up. Badly.
	if x == 0:
		print("You screwed up badly.")
		new_x = input("Try again: ")
		rec = multiplicative_inverse(int(new_x))
		return rec
	rec = x ** -1
	return rec

# TODO: Write tests for multiplicative_inverse.
test_value_0 = multiplicative_inverse()
assert 2 + 4 == 6
test_value_1 = multiplicative_inverse(5)
assert test_value_1 == 0.2
test_value_2 = multiplicative_inverse(10)
assert test_value_2 == 0.1
test_value_3 = multiplicative_inverse(0.5)
assert test_value_3 == 2
test_value_4 = multiplicative_inverse(1/4)
assert test_value_4 == 4
#test_value_5 = multiplicative_inverse(2/0)
#print(test_value_5) # ERROR? 0/2?
test_value_6 = multiplicative_inverse(0)
print(test_value_6) # ERROR? 0/0?

value = int(input("Give me a number to find its multiplicative inverse: "))
print(multiplicative_inverse(value))


def reciprocal(numerator, denominator):
	# Returns the reciprocal of a fraction with given numerator and denominator.
	# TODO: Handle edge cases and invalid inputs.
	rec = numerator / denominator ** -1
	return rec

# TODO: Write tests for reciprocal