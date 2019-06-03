from random import randint


class RandomPlayer(object):

    def __init__(self, name="Random Player"):
        self.name = name

    def __repr__(self):
        return self.name

    def make_move(self, nimbers, max_take):
        if max_take >= nimbers:
            take = nimbers
        else:
            take = min(randint(1, max_take) for _ in range(3))
        return take
