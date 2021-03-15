def k_means(examples, k, verbose=False):
    # Get k randomly chosen initial centroids, create cluster for each
    initial_centroids = random.sample(examples, k)
    clusters = []
    for e in initial_centroids:
        clusters.append(Cluster([e]))

    # Iterate until centroids do not change
    converged = False
    num_iterations = 0
    while not converged:
        num_iterations += 1
        # Create a list containing k distinct empty lists
        new_clusters = []
        for i in range(k):
            new_clusters.append([])

        # Associate each example with closest centroid
        for e in examples:
            # Find the centroid closest to e
            smallest_distance = e.distance(clusters[0].get_centroid())
            index = 0
            for i in range(1, k):
                distance = e.distance(clusters[i].get_centroid())
                if distance < smallest_distance:
                    smallest_distance = distance
                    index = i
            # Add e to the list of examples for appropriate cluster
            new_clusters[index].append(e)

        for c in new_clusters:  # Avoid having empty clusters
            if len(c) == 0:
                raise ValueError('Empty Cluster')

        # Update each cluster; check if a centroid has changed
        converged = True
        for i in range(k):
            if clusters[i].update(new_clusters[i]) > 0.0:
                converged = False

        if verbose:
            print('Iteration #' + str(num_iterations))
            for c in clusters:
                print(c)
            print('')  # add blank line
    return clusters
