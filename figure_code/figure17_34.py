def sim_insertions(num_indices, num_insertions):
    '''Assumes num_indices and num_insertions are positive ints.
    Returns 1 if there is a collision; 0 otherwise'''
    choices = range(num_indices)  # list of possible indices
    used = []
    for i in range(num_insertions):
        hash_val = random.choice(choices)
        if hash_val in used:  # there is a collision
            return 1
        else:
            used.append(hash_val)
    return 0


def find_prob(num_indices, num_insertions, num_trials):
    collisions = 0
    for t in range(num_trials):
        collisions += sim_insertions(num_indices, num_insertions)
    return collisions/num_trials
