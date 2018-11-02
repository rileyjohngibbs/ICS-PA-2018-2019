# What are the keys of the dictionary `players`?
# What is the output of this program when it is run?

players = {
    "Erik": "paladin",
    "Jordan": "ranger",
    "Michelle": "wizard",
    "Nick": "bard",
    "Zack": "warlock",
}

players["Kaelen"] = "wizard"

you = input("Who are you? ")
you_class = input("WHat are you playing? ")
players[you] = you_class

for name in players:
    print(f"{name} is playing a {players[name]}.")

people = ["Erik", "Zack", "Karen", "Mor", "Johnny"]
for person in people:
    print(f"{person} is {players.get(person, 'not playing')}.")

# mystery_key = input("Ask for a player: ")

"""
if mystery_key in players:
    print(f"{mystery_key} is one of my players! They are playing a {players[mystery_key]}.")
else:
    print(f"{mystery_key} is not one of my players. Sorry!")
"""

paragraphs = """Once upon a time there was a moo cow and the moo cow was walking down the road.
One day the moo cow made a new friend.
They lived happily ever after."""
















# What type of values does the dictionary `players_complete` have?

players_complete = {
    "Erik": {
        "race": "human",
        "class": "paladin",
        "level": 3,
    },
    "Jordan": {
        "race": "elf",
        "class": "ranger",
        "level": 4,
    },
    "Michelle": {
        "race": "human",
        "class": "wizard",
        "level": 3,
    },
    "Nick": {
        "race": "gnome",
        "class": "bard",
        "level": 4,
    },
    "Zack": {
        "race": "tiefling",
        "class": "warlock",
        "level": 4,
    },
}