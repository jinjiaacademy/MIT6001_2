def prevalence_classify(training_set, test_set, label):
    '''Assumes training_set & test_set lists of examples
    Uses a prevalence-based classifier to predict
    whether each example in test_set is of class label
    Returns number of true positives, false positives,
    true negatives, and false negatives'''
    num_with_label = 0
    for e in training:
        if e.get_label() == label:
            num_with_label += 1
    prob_label = num_with_label/len(training_set)
    true_pos, false_pos, true_neg, false_neg = 0, 0, 0, 0
    for e in test_set:
        if random.random() < prob_label:
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
