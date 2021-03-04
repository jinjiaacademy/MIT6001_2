class Cold_drunk(Drunk):
    def take_step(self):
        stepChoices = [(0.0, 1.0), (0.0, -2.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)


class EW_drunk(Drunk):
    def take_step(self):
        stepChoices = [(1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)


def sim_all(drunk_kinds, walk_lengths, num_trials):
    for d_class in drunk_kinds:
        drunk_test(walk_lengths, num_trials, d_class)
