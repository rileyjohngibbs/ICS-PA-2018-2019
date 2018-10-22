import random
from typing import Iterable, List


def main() -> None:
	students = list(multi_input("Attendance: "))
	random.shuffle(students)
	pairs = make_pairs(students)
	for pair in pairs:
		print(pair)


def multi_input(message: str) -> Iterable[str]:
	print(message)
	while True:
		name = input()
		if name == "":
			break
		yield name


def make_pairs(students: List[str]) -> List[List[str]]:
	if len(students) % 2 == 0:
		pairs = [
			[students[i], students[i+1]]
			for i in range(0, len(students), 2)	
		]
	else:
		pairs = [
			[students[i], students[i+1]]
			for i in range(0, len(students) - 3, 2)
		] + [students[-3:]]
	return pairs


if __name__ == "__main__":
	main()