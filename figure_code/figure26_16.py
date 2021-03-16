def apply_model(model, test_set, label, prob = 0.5):
    # Create vector containing feature vectors for all test examples
    test_feature_vecs = [e.get_features() for e in test_set]
    probs = model.predict_proba(test_feature_vecs)
    true_pos, false_pos, true_neg, false_neg = 0, 0, 0, 0
    for i in range(len(probs)):
        if probs[i][1] > prob:
            if test_set[i].get_label() == label:
                true_pos += 1
            else:
                false_pos += 1
        else:
            if test_set[i].get_label() != label:
                true_neg += 1
            else:
                false_neg += 1
    return true_pos, false_pos, true_neg, false_neg

random.seed(0)

examples = build_marathon_examples('bm_results2012.csv')
training, test = divide_80_20(examples)

feature_vecs, labels = [], []
for e in training:
    feature_vecs.append([e.get_age(), e.get_time()])
    labels.append(e.get_label())
model = sklm.LogisticRegression().fit(feature_vecs,labels)
print('Feature weights for label M:',
      'age =', str(round(model.coef_[0][0], 3)) + ',',
      'time =', round(model.coef_[0][1], 3))
true_pos, false_pos, true_neg, false_neg = \
                      apply_model(model, test, 'M', 0.5)
get_stats(true_pos, false_pos, true_neg, false_neg)

