def dissimilarity(clusters):
    tot_dist = 0.0
    for c in clusters:
        tot_dist += c.variability()
    return tot_dist


def try_k_means(examples, num_clusters, num_trials, verbose=False):
    '''Calls k_means num_trials times and returns the result with the
    lowest dissimilarity'''
    best = k_means(examples, num_clusters, verbose)
    min_dissimilarity = dissimilarity(best)
    trial = 1
    while trial < num_trials:
        try:
            clusters = k_means(examples, num_clusters, verbose)
        except ValueError:
            continue  # if failed, try again
        curr_dissililarity = dissimilarity(clusters)
        if curr_dissililarity < min_dissimilarity:
            best = clusters
            min_dissimilarity = curr_dissililarity
        trial += 1
    return best
