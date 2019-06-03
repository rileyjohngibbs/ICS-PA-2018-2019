from nimbers.nimbers import Nimbers
from nimbers.human import Human
from nimbers.randomplayer import RandomPlayer


if __name__ == "__main__":
    player_count = "A"
    while not player_count.isdigit() or not int(player_count) in [1, 2]:
        player_count = input("How many human players? [1, 2] ")
    if player_count == "1":
        game = Nimbers(Human(input("Name? ")), RandomPlayer())
    else:
        game = Nimbers(
            Human(input("Name of first player? ")),
            Human(input("Name of second player? "))
        )
    game.play()
