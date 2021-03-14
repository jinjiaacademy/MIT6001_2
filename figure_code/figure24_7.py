class Animal(object):
    def __init__(self, name, features):
        '''Assumes name a string; features a list of numbers'''
        self.name = name
        self.features = np.array(features)

    def get_name(self):
        return self.name

    def get_features(self):
        return self.features

    def distance(self, other):
        '''Assumes other is an Animal
        Returns the Euclidean distance between feature vectors
        of self and other'''
        return minkowski_dist(self.get_features(),
                              other.get_features(), 2)
