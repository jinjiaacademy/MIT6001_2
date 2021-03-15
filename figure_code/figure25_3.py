class Cluster(object):
    def __init__(self, examples):
        '''Assumes examples a non-empty list of Examples'''
        self.examples = examples
        self.centroid = self.compute_centroid()

    def update(self, examples):
        '''Assumes examples is a non-empty list of Examples
        Replace examples; retrun amount centroid has changed'''
        old_centroid = self.centroid
        self.examples = examples
        self.centroid = self.compute_centroid()
        return old_centroid.distance(self.centroid)

    def compute_centroid(self):
        vals = np.array([0.0]*self.examples[0].dimensionality())
        for e in self.examples:
            vals += e.get_features()
        centroid = Example('centroid', vals/len(self.examples))
        return centroid

    def get_centroid(self):
        return self.centroid

    def variability(self):
        tot_dist = 0.0
        for e in self.examples:
            tot_dist += (e.distance(self.centroid))**2
        return tot_dist

    def members(self):
        for e in self.examples:
            yield e

    def __str__(self):
        names = []
        for e in self.examples:
            names.append(e.get_name())
        names.sort()
        result = ('Cluster with centroid '
                  + str(self.centroid.get_features()) + ' contains:\n ')
        for e in names:
            result = result + e + ', '
        return result[:-2]
