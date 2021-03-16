def find_k(training_set, min_k, max_k, num_folds, label):
    # Find average accuracy for range of odd values of k
    accuracies = []
    for k in range(min_k, max_k + 1, 2):
        score = 0.0
        for i in range(num_folds):
            # downsample to reduce computation time
            fold = random.sample(training_set,
                                 min(5000, len(training_set)))
            examples, test_set = divide_80_20(fold)
            true_pos, false_pos, true_neg, false_neg =\
                k_nearest_classify(examples, test_set, label, k)
            score += accuracy(true_pos, false_pos, true_neg, false_neg)
        accuracies.append(score/num_folds)
    plt.plot(range(min_k, max_k+1, 2), accuracies)
    plt.title('Average Accuracy vs k (' + str(num_folds)
              + ' folds)')
    plt.xlabel('k')
    plt.ylabel('Accuracy')
    plt.show()


find_k(training, 1, 21, 5, 'M')
