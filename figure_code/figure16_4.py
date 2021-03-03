def walk(f, d, num_steps):
    '''Assumes: f a Field, d a Drunk in f, and num_steps an int >= 0.
    moves d num_steps times; returns the distance between the
    final location and the location at the start of the walk.'''
    start = f.get_loc(d)
    for s in range(num_steps):
        f.move_drunk(d)
    return start.dist_from(f.get_loc(d))


def sim_walks(num_steps, num_trials, d_class):
    '''Assumes num_steps an int >= 0, num_trails an int > 0,
    d_class a subclass of Drunk
    Simulates num_trials walks of num_steps steps each.
    Returns a list of the final distances for each trial'''
    Homer = d_class()
    origin = Location(0, 0)
    distances = []
    for t in range(num_trials):
        f = Field()
        f.add_drunk(Homer, origin)
        distances.append(round(walk(f, Homer, num_trials), 1))
    return distances


def drunk_test(walk_lengths, num_trials, d_class):
    '''Assumes walk_lengths a sequence of ints >= 0
    num_trials an int > 0, d_class a subclass of Drunk
    For each number of steps in walk_lengths, runs sim_walks with
    num_trials walks and prints results'''
    for num_steps in walk_lengths:
        distances = sim_walks(num_steps, num_trials, d_class)
        print(d_class.__name__, 'walk of', num_steps, 'steps: Mean =',
              f'{sum(distances)/len(distances):.3f}, Max =',
              f'{max(distances)}, Min = {min(distances)}')
