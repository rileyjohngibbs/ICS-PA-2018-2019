from random import randint
import time

# TODO: Pick range of temperatures for new soup.
# TODO: Set conditions for each opinion.
# TODO: Get this to actually do something when it's run.
# TODO: Ask user if they want to try new soup instead of doing it automatically.


def main():
	opinion = None
	while opinion != "just right":
		soup_temp = new_soup()
		opinion = temperature_check(soup_temp)
		print(f"This soup is {soup_temp}°F. It is {opinion}!")
		time.sleep(2)
	print("Ah, delicious!")


def new_soup():
	soup_temp = randint(__, __) # TODO: Complete this line
	return soup_temp


def temperature_check(temp):
	if _____: # TODO: Complete this line
		opinion = "too cold"
	elif _____: # TODO: Complete this line
		opinion = "too hot"
	else:
		opinion = "just right"
	return opinion
