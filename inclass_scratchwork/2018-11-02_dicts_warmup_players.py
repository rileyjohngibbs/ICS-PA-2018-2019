# How would you retrieve Michelle's level from this dictionary?
# How would you change Michelle's level to 4 in this dictionary?

players = {
    "Erik": {
        "race": "human",
        "class": "paladin",
        "level": 3,
        "name": "Erikunu",
    },
    "Jordan": {
        "race": "elf",
        "class": "ranger",
        "level": 4,
        "name": "Solaris",
    },
    "Michelle": {
        "race": "human",
        "class": "wizard",
        "level": 3,
        "name": "Shayera",
    },
    "Nick": {
        "race": "gnome",
        "class": "bard",
        "level": 4,
        "name": "Randy",
    },
    "Zack": {
        "race": "tiefling",
        "class": "warlock",
        "level": 4,
        "name": "Thaliondil",
    },
}

# Goal: Write a program that adds a new player, defined by the user, to this dictionary of players. We'll have to ask the user about this new player, getting their race, class, level, and name. The program then reports all the current players, telling us their real name, their race, their class, their level, and their character name.

# Think and write: Broadly speaking, what are the steps we have to take to accomplish adding a new user-defined player to the dictionary?





























# Write a function that asks for a race, class, level, and name from the user; puts all those values in a dictionary; then returns that dictionary.

players[real_name] = character_info
