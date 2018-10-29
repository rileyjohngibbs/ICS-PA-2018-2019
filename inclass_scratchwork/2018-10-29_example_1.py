a = 0
b = 0
c = 0


def foo():
	global a
	x = input("Give me a number: ")
	a = float(x)
	bar()


def bar():
	global b
	y = input("Give me a number: ")
	b = float(y)


def main():
	global c
	print("Let's do some math!")
	foo()
	c = a ** b


main()
print(f"I did some math with your numbers and I got {c}.")
