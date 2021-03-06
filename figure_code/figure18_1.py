import random
import numpy as np


def roll_die():
    # return random.choice([1, 2, 3, 4, 5, 6])
    return random.choice([1, 1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6])


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


def craps_sim(hands_per_game, num_games):
    '''Assumes hands_per_game and num_games are ints > 0
    Play num_games games of hands_per_game hands; print results'''
    games = []

    # Play num_games games
    for t in range(num_games):
        c = Craps_game()
        for i in range(hands_per_game):
            c.play_hand()
        games.append(c)

    # Produce statistics for each game
    p_ROI_per_game, dp_ROI_per_game = [], []
    for g in games:
        wins, losses = g.pass_results()
        p_ROI_per_game.append((wins-losses)/float(hands_per_game))
        wins, losses, pushes = g.dp_results()
        dp_ROI_per_game.append((wins-losses)/float(hands_per_game))

    # Produce and print summary statistics
    mean_ROI = str(round((100*sum(p_ROI_per_game)/num_games), 4)) + '%'
    sigma = str(round(100*np.std(p_ROI_per_game), 4)) + '%'
    print('Pass:', 'Mean ROI =', mean_ROI, 'Std. Dev. =', sigma)
    mean_ROI = str(round((100*sum(dp_ROI_per_game)/num_games), 4)) + '%'
    sigma = str(round(100*np.std(dp_ROI_per_game), 4)) + '%'
    print('Don\'t pass:', 'Mean ROI =', mean_ROI, 'Std Dev =', sigma)


# check_pascal(1000000)
craps_sim(1000000, 10)
