import random
import pandas as pd


class Passenger(object):
    features = ('1st Class', '2nd Class', '3rd Class',
                'age', 'male')
    def __init__(self, pClass, age, gender, survived, name):
        self._name = name
        self._feature_vec = [0, 0, 0, age, gender]
        self._feature_vec[pClass - 1] = 1
        self._label = survived
        self.cabinClass = pClass
    def distance(self, other):
        return minkowski_dist(self.veatureVec, other._feature_vec, 2)
    def get_class(self):
        return self.cabinClass
    def get_age(self):
        return self._feature_vec[3]
    def get_gender(self):
        return self._feature_vec[4]
    def get_name(self):
        return self._name
    def get_features(self):
        return self._feature_vec[:]
    def get_label(self):
        return self._label

# # Figure 26-20 on page 615
def build_Titanic_examples():
    manifest = pd.read_csv('TitanicPassengers.csv')
    examples = []
    for index, row in manifest.iterrows():
        p = Passenger(row['Class'], row['Age'],
                      1 if row['Gender'] == 'M' else 0,
                      row['Survived'],
                      row['Last Name'] + row['Other Names'])
        examples.append(p)
    return examples

# # Figure 26-21 on page 616
def test_models(examples, num_trials, print_stats, print_weights):
    stats, weights = [], [[], [], [], [], []]
    for i in range(num_trials):
        training, test_set = divide_80_20(examples)
        xVals, yVals = [], []
        for e in training:
            xVals.append(e.get_features())
            yVals.append(e.get_label())
        xVals = np.array(xVals)
        yVals = np.array(yVals)
        model = sklm.LogisticRegression().fit(xVals, yVals)
        for i in range(len(Passenger.features)):
            weights[i].append(model.coef_[0][i])
        true_pos, false_pos, true_neg, false_neg =\
                         apply_model(model, test_set, 1, 0.5)
        auroc = build_ROC(model, test_set, 1, None, False)
        tmp = get_stats(true_pos, false_pos, true_neg, false_neg, False)
        stats.append(tmp + (auroc,))
    print('Averages for', num_trials, 'trials')
    if print_weights:
        for feature in range(len(weights)):
            feature_mean = round(sum(weights[feature])/num_trials, 3)
            feature_std = np.std(weights[feature])
            print(' Mean weight', Passenger.features[feature],
              '=', str(feature_mean) + ', 95% conf. int. =',
              round(feature_mean - 1.96*feature_std, 3), 'to',
              round(feature_mean + 1.96*feature_std, 3))
    if print_stats:
        summarize_stats(stats)

# # Figure 26-22 on page 617
def summarize_stats(stats):
    """assumes stats a list of 5 floats: accuracy, sensitivity,
       specificity, pos. pred. val, ROC"""
    def print_stat(X, name):
        mean = round(sum(X)/len(X), 3)
        std = np.std(X)
        print(' Mean', name, '=', str(mean) + ',',
               '95% conf. int. =',
               round(mean - 1.96*std, 3), 'to',
               round(mean + 1.96*std, 3))
    accs, sens, specs, ppvs, aurocs = [], [], [], [], []
    for stat in stats:
        accs.append(stat[0])
        sens.append(stat[1])
        specs.append(stat[2])
        ppvs.append(stat[3])
        aurocs.append(stat[4])
    print_stat(accs, 'accuracy')
    print_stat(sens, 'sensitivity')
    print_stat(accs, 'specificity')
    print_stat(sens, 'pos. pred. val.')
    print_stat(aurocs, 'AUROC')

# # Code from page 617
random.seed(0)
test_models(build_Titanic_examples(), 100, True, False)
test_models(build_Titanic_examples(), 100, False, True)
