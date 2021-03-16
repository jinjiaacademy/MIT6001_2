import random
import sklearn.linear_model as sklm


feature_vecs, labels = [], []
for i in range(25000):
    feature_vecs.append([random.gauss(0, 0.5), random.gauss(0, 0.5),
                         random.random()])
    labels.append('A')
    feature_vecs.append([random.gauss(0, 0.5), random.gauss(2, 0.5),
                         random.random()])
    labels.append('B')
    feature_vecs.append([random.gauss(2, 0.5), random.gauss(0, 0.5),
                         random.random()])
    labels.append('C')
    feature_vecs.append([random.gauss(2, 0.5), random.gauss(2, 0.5),
                         random.random()])
    labels.append('D')

model = sklm.LogisticRegression().fit(feature_vecs, labels)
print('model.classes =', model.classes_)

for i in range(len(model.coef_)):
    print('For label', model.classes_[i],
          'feature weights =', model.coef_[i].round(4))

print('[0, 0] probs =', model.predict_proba([[0, 0, 1]])[0].round(4))
print('[0, 2] probs =', model.predict_proba([[0, 2, 2]])[0].round(4))
print('[2, 0] probs =', model.predict_proba([[2, 0, 3]])[0].round(4))
print('[2, 2] probs =', model.predict_proba([[2, 2, 4]])[0].round(4))

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
