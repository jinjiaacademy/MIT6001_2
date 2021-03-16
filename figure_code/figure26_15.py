feature_vecs, labels = [], []
for i in range(20000):
    feature_vecs.append([random.gauss(0, 0.5), random.gauss(0, 0.5)])
    labels.append('A')
    feature_vecs.append([random.gauss(2, 0.5), random.gauss(2, 0.5)])
    labels.append('D')


model = sklm.LogisticRegression().fit(feature_vecs, labels)
print('model.coef =', model.coef_.round(4))
print('[0, 0] probs =', model.predict_proba([[0, 0]])[0].round(4))
print('[0, 2] probs =', model.predict_proba([[0, 2]])[0].round(4))
print('[2, 0] probs =', model.predict_proba([[2, 0]])[0].round(4))
print('[2, 2] probs =', model.predict_proba([[2, 2]])[0].round(4))
