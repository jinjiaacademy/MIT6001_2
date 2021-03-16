def find_k_nearest(example, example_set, k):
    k_nearest, distances = [], []
    # Build lists containing first k examples and their distances
    for i in range(k):
        k_nearest.append(example_set[i])
        distances.append(example.feature_dist(example_set[i]))
    max_dist = max(distances)  # Get maximum distance
    # Look at examples not yet considered
    for e in example_set[k:]:
        dist = example.feature_dist(e)
        if dist < max_dist:
            # replace farther neighbor by this one
            max_index = distances.index(max_dist)
            k_nearest[max_index] = e
            distances[max_index] = dist
            max_dist = max(distances)
    return k_nearest, distances


def k_nearest_classify(training_set, test_set, label, k):
    '''Assumes training_set & test_set lists of examples, k an int
    Uses a k-nearest neighbor classifier to predict
    whether each example in test_set has the given label
    Returns number of true positives, false positives,
    true negatives, and false negatives'''
    true_pos, false_pos, true_neg, false_neg = 0, 0, 0, 0
    for e in test_set:
        print('Classifying', e)
        nearest, distances = find_k_nearest(e, training_set, k)
        # conduct vote
        num_match = 0
        for i in range(len(nearest)):
            if nearest[i].get_label() == label:
                num_match += 1
        if num_match > k//2:  # guess label
            if e.get_label() == label:
                true_pos += 1
            else:
                false_pos += 1
        else:
            if e.get_label() != label:
                true_neg += 1
            else:
                false_neg += 1
    return true_pos, false_pos, true_neg, false_neg
