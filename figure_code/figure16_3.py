class Drunk(object):
    def __init__(self, name=None):
        '''Assumes name is a str'''
        self._name = name

    def __str__(self):
        if self != None:
            return self._name
        return 'Anonymous'


class Usual_drunk(Drunk):
    def take_step(self):
        step_choices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(step_choices)
        return random.choice(step_choices)
