def make_greeting(name, time_of_day):
    if time_of_day == "morning":
        greeting = make_morning_greeting(name)
    elif time_of_day == "afternoon":
        greeting = make_afternoon_greeting(name)
    elif time_of_day == "evening":
        greeting = make_evening_greeting(name)
    else:
        greeting = make_anytime_greeting(name)
    return greeting


def make_morning_greeting(person):
    message = f"Good morning, {person}!"
    return message


def make_afternoon_greeting(person):
    # TODO: Make the message and return it
    pass

# TODO: Write make_evening_greeting function


# TODO: Write make_anytime_greeting function


your_name = input("What's your name? ")
morning_greeting = make_greeting(your_name, "morning")
afternoon_greeting = make_greeting(your_name, "afternoon")
evening_greeting = make_greeting(your_name, "evening")
anytime_greeting = make_greeting(your_name, "brillig")


# TODO: Guess what each greeting will be

assert morning_greeting == _____
print(morning_greeting)

assert afternoon_greeting == _____
print(afternoon_greeting)

assert evening_greeting == _____
print(evening_greeting)

assert anytime_greeting == _____
print(anytime_greeting)