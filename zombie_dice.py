from random import randint

'''
Features
- Player can roll a die and get a result of caught, ran, or fought. DONE
- Player can roll three dice at a time. DONE
- Player can keep rolling and accumulate a point for every 'caught' result. DONE
- Player's turn ends with 0 points if they accumulate three 'fought' results. DONE
- Player can end turn early. DONE
- Player keeps their points from turn to turn. DONE
- Two or more players can play.
- Game ends at the end of a round if a player has 13 or more points.
- Players can get dice with different probabilities, selected randomly.
'''


def main():
    player = Player()
    keep_playing = True
    player.take_turn()
    while keep_playing:  # TODO: Fix bug: The game won't let the player only take one turn.
        player.take_turn()
        keep_playing = ask_yes_no('Keep playing?')


class Die(object):

    def __init__(self):
        self.value = 'ran'

    def roll(self):
        number = randint(1, 6)
        if number == 1:
            self.value = 'fought'
        elif 2 <= number <= 4:  # How sure am I that this works right?
            self.value = 'ran'
        else:  # Should I be more explicit here and use "elif number >= 5:" instead?
            self.value = 'caught'


class Player(object):

    def __init__(self):
        self.score = 0

    def take_turn(self):
        print(f'Your current total score is {self.score}.')
        roll_again = True
        turn_score = 0
        fought_rolls = 0
        while roll_again and fought_rolls < 3:
            print('-' * 20)
            rolls = self.roll()
            roll_score = 0  # Maybe I should calculate roll_score in its own method?
            for roll in rolls:
                print(f'Your rolled a "{roll}".')
                if roll == 'caught':
                    roll_score += 1
                if roll == 'fought':
                    fought_rolls += 1
            print(f'You scored {roll_score} points.')
            turn_score += roll_score
            print(f'Your turn score is now {turn_score} points and have gotten {fought_rolls} fought rolls.')
            roll_again = ask_yes_no('Roll again?')  # TODO: Don't ask if they want to roll again if they've rolled 3 foughts.
        if fought_rolls < 3:
            self.score += turn_score
        else:
            print(f'You rolled too many fought rolls and got no points this turn.')
        print(f'Your total score is now {self.score}.')
        print('=' * 20)

    def roll(self):
        dice = [Die(), Die(), Die()]
        for die in dice:
            die.roll()
        return [die.value for die in dice]


def ask_yes_no(question):  # TODO: My questions look like this: "Do you want chocolate?yes". I want a space between my question and the user's answer.
    answer = ''
    while answer.lower() not in ['yes', 'y', 'no', 'n']:
        answer = input(question)
    if answer in ['yes', 'y']:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
