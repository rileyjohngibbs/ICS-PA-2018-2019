def ask_for_number():
	num = input(f"Give me a number: ")
	return float(num)


def square_their_numbers():
	base = ask_for_number()
	exponent = ask_for_number()
	return base ** exponent


def main():
	print("Let's do some math!")
	result = square_their_numbers()
	print(f"I did some math with your numbers and I got {result}.")


main()
