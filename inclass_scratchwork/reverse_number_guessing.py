from sys import exit
from typing import List, Optional, Tuple, Union


def main() -> None:
    min_, max_ = 0, 500
    print(f"Think of a number from {min_} to {max_}. I will try to guess in 10 guesses or less.")
    correct = False
    guess_count = 0
    while not correct:
        guess, feedback = try_guess(min_, max_)
        guess_count += 1
        if feedback == "greater":
            min_ = guess + 1
        elif feedback == "less":
            max_ = guess - 1
        elif feedback == "equal":
            correct = True
        if min_ > max_:
            handle_impossibility(min_, max_)
    print(f"I got it in {guess_count} tries! Thank you for playing with me.")


def try_guess(min_: int, max_: int) -> Tuple[int, str]:
    guess = int((min_ + max_) / 2)
    question = f"My guess is {guess}. Is your number greater, less, or equal? "
    options = ["greater", "less", "equal"]
    feedback = ask(question, options)
    return guess, feedback


def ask(msg: str, options: List[str]) -> str:
    answer: Optional[str] = None
    while answer not in options:
        answer = input(msg)
    return answer


def handle_impossibility(min_: int, max_: int) -> None:
    print(f"Uh-oh. Either you cheated or you made a mistake. Based on the rules, your number must be at least {min_} but no more than {max_}, which is impossible! Maybe we can try playing again another time.")
    exit(0)


if __name__ == "__main__":
    main()