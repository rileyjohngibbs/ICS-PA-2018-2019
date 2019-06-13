import math


class ArtificialIntelligence(object):

    def __init__(self, name="Andy the Android"):
        self.name = name

    def __repr__(self):
        return self.name

    def make_move(self, nimbers, max_take):
        if nimbers <= max_take:
            return nimbers
        target = self.find_highest_fib(nimbers)
        needed = nimbers - target
        if needed <= max_take:
            return max(1, min(needed, math.ceil(nimbers/3) - 1))
        else:
            return self.make_move(needed, max_take)

    def find_highest_fib(self, top):
        gen = self.fib_gen()
        fib = 0
        candidate = next(gen)
        while candidate < top:
            fib = candidate
            candidate = next(gen)
        return fib

    def fib_gen(self):
        a, b = 0, 1
        while True:
            yield b
            a, b = b, a + b
