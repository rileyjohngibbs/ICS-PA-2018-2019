class Human(object):

    def __init__(self, name="Fleshbag"):
        self.name = name

    def __repr__(self):
        return self.name

    def make_move(self, nimbers, max_take):
        print(f"There are {nimbers} nimbers left. You can take up to {max_take}.")
        take = "A"
        while not take.isdigit():
            take = input("How many nimbers do you want to take? ")
        return int(take)
