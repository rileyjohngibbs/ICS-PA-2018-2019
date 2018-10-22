from random import randint
from re import match
from sys import argv, exit
from typing import Optional, Tuple

def main() -> None:
    min_, max_ = get_min_max()
    secret_number = randint(min_, max_)
    guess = None
    while guess != secret_number:
        guess = get_guess(min_, max_)
        feedback = give_feedback(secret_number, guess)
        print(feedback)


def get_min_max() -> Tuple[int, int]:
    if len(argv) >= 3:
        try:
            min_ = int(argv[1])
            max_ = int(argv[2])
        except ValueError:
            print("Usage: python number_guessing.py [<min_number> <max_number>]")
            exit(1)
    elif len(argv) == 2:
        print("Usage: python number_guessing.py [<min_number> <max_number>]")
        exit(1)
    else:
        min_ = 0
        max_ = 1000
    return min_, max_

def get_guess(min_: int, max_: int) -> int:
    raw_guess = ""
    while not match(r"-?[0-9]+$", raw_guess):
        raw_guess = input(f"Guess an integer from {min_} and {max_}: ")
    return int(raw_guess)


def give_feedback(secret_number: int, guess: int) -> Optional[str]:
    if guess < secret_number:
        return f"The secret number is greater than {guess}."
    elif guess > secret_number:
        return f"The secret number is less than {guess}."
    else:
        return f"Great guess! The secret number is {secret_number}. Thank you for playing with me!"


if __name__ == "__main__":
    main()