class DoublingNim(object):

    def __init__(self, first_player, second_player):
        self.first = first_player
        self.second = second_player
        self.nimbers = 0
        self.max_take = 0
        self.active_player = None

    def play(self, nimbers=100):
        self.nimbers = nimbers
        self.max_take = nimbers - 1
        self.active_player = self.first
        while self.nimbers > 0:
            self.take_turn()
            self.active_player = self.second if self.active_player is self.first else self.first
        winner = self.second if self.active_player is self.first else self.first
        print(f"{winner} wins!")

    def take_turn(self):
        valid_move = False
        taken = 0
        while valid_move is False:
            taken = self.active_player.make_move(self.nimbers, self.max_take)
            if taken > self.max_take or taken < 1:
                print(f"Illegal move. You may not take more than {self.max_take} nimbers, and you must take at least 1 nimber.")
            else:
                valid_move = True
        self.nimbers -= taken
        self.max_take = min(taken * 2, self.nimbers)
        print(f"{self.active_player} has taken {taken} nimbers.")
        print("-" * 20)
