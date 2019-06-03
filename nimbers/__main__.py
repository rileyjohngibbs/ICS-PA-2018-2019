from nimbers.nimbers import Nimbers
from nimbers.human import Human
from nimbers.randomplayer import RandomPlayer
from nimbers.aiplayer import ArtificialIntelligence


if __name__ == "__main__":
    player_count = "A"
    while not player_count.isdigit() or not int(player_count) in [1, 2]:
        player_count = input("How many human players? [1, 2] ")
    if player_count == "1":
        try:
            ai = ArtificialIntelligence()
            ai.make_move(5, 3)
            game = Nimbers(Human(input("Name? ")), ai)
        except NotImplementedError:
            game = Nimbers(Human(input("Name? ")), RandomPlayer())
    else:
        game = Nimbers(
            Human(input("Name of first player? ")),
            Human(input("Name of second player? "))
        )
    nimber_count = "A"
    while not nimber_count.isdigit() or nimber_count == "0":
        nimber_count = input("How many starting nimbers? ")
    game.play(int(nimber_count))
