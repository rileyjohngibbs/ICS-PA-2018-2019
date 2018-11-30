from random import randint


STRENGTHS = {
    "grass": "water",
    "water": "fire",
    "fire": "grass"
}


class Pokemon(object):

    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_
        self.hp = 50

    def attack(self, target):
        base_damage = self.roll_damage()
        damage = self.modify_damage(base_damage, target)
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)

    def roll_damage(self):
        return randint(1, 10) + randint(1, 10)

    def modify_damage(self, base_damage, target):
        strength = STRENGTHS[self.type_]
        target_strength = STRENGTHS[target.type_]
        if strength == target.type_:
            damage = base_damage * 2
        if target_strength == self.type_:
            damage = int(base_damage / 2)
        return damage

    def take_damage(self, damage):
        self.hp = max(self.hp - damage, 0)
        if self.hp == 0:
            print(f"{self.name} has fainted!")


bulbasaur = Pokemon("Bulbasaur", "grass")
charmander = Pokemon("Charmander", "fire")
squirtle = Pokemon("Squirtle", "water")