from random import randint


def ask_to_continue():
    pass


def roll_two_dice():
    pass


def calculate_score(total):
    pass


def main():
    total = roll_two_dice()
    print(f"Your starting amount is {total}.")
    roll_again = ask_to_continue()

    if roll_again == "yes":
        new_roll = roll_two_dice()
        total += new_roll
        print(f"You rolled {new_roll}. Your new total is {total}.")

    score = calculate_score(total)
    print(f"Your final total was {total} and your score is {score}!")


main()