import random
import numpy as np


def roll_die():
    return random.choice([1, 2, 3, 4, 5, 6])


def check_pascal(num_trials):
    '''Assumes num_trials is an int > 0
    Prints an estimate of the probability of winning'''
    num_wins = 0
    for i in range(num_trials):
        for j in range(24):
            d1 = roll_die()
            d2 = roll_die()
            if d1 == 6 and d2 == 6:
                num_wins += 1
                break
    print('Probability of winning =', num_wins/num_trials)


class Craps_game(object):
    def __init__(self):
        self.pass_wins, self.pass_losses = 0, 0
        self.dp_wins, self.dp_losses, self.dp_pushes = 0, 0, 0

    def play_hand(self):
        throw = roll_die() + roll_die()
        if throw == 7 or throw == 11:
            self.pass_wins += 1
            self.dp_losses += 1
        elif throw == 2 or throw == 3 or throw == 12:
            self.pass_losses += 1
            if throw == 12:
                self.dp_pushes += 1
            else:
                self.dp_wins += 1
            else:
                point = throw
                while True:
                    throw = roll_die() + roll_die()
                    if throw == point:
                        self.pass_wins += 1
                        self.dp_losses += 1
                        break
                    elif throw == 7:
                        self.pass_losses += 1
                        self.dp_wins += 1
                        break

    def pass_results(self):
        return (self.pass_wins, self.pass_losses)
    def dp_results(self):
        return (self.dp_wins, self.dp_losses, self.dp_pushes)
















# check_pascal(1000000)
