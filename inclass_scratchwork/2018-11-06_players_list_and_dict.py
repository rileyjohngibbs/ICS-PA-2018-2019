players_dict = {
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

for player in players_dict:
    print(player)
    print(players_dict[player]) # Print their whole character information
    print(players_dict[player]["level"]) # Print their level only






players_list = [
    {
        "race": "human",
        "class": "paladin",
        "level": 3,
        "player_name": "Erik",
        "character_name": "Erikunu",
    },
    {
        "race": "elf",
        "class": "ranger",
        "level": 4,
        "player_name": "Jordan",
        "character_name": "Solaris",
    },
    {
        "race": "human",
        "class": "wizard",
        "level": 3,
        "player_name": "Michelle",
        "character_name": "Shayera",
    },
    {
        "race": "gnome",
        "class": "bard",
        "level": 4,
        "player_name": "Nick",
        "character_name": "Randy",
    },
    {
        "race": "tiefling",
        "class": "warlock",
        "level": 4,
        "player_name": "Zack",
        "character_name": "Thaliondil",
    },
]

#for player in player_list:
    #print(player)