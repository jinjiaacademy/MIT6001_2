import random
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


def get_BM_data(filename):
    '''Read the contents of the given file. Assumes the file is
    in a comma-separated format, with 6 elements in each entry:
    0. Name (string), 1. Gender (string), 2. Age (int),
    3. Division (int), 4. Country (string), 5. Overall time (float)
    Returns: dict containing a list for each of the 6 variables.'''
    data = {}
    with open(filename, 'r') as f:
        f.readline()  # discard first line
        line = f.readline()
        for k in ('name', 'gender', 'age', 'division',
                  'country', 'time'):
            data[k] = []
        while line != '':
            split = line.split(',')
            data['name'].append(split[0])
            data['gender'].append(split[1])
            data['age'].append(split[2])
            data['division'].append(split[3])
            data['country'].append(split[4])
            data['time'].append(float(split[5][:-1]))  # remove \n
            line = f.readline()
    return data


def make_hist(data, bins, title, xLabel, yLabel):
    plt.hist(data, bins)
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    mean = sum(data)/len(data)
    std = np.std(data)
    plt.annotate('Mean = ' + str(round(mean, 2)) +
                 '\nSD = ' + str(round(std, 2)), fontsize=14,
                 xy=(0.65, 0.75), xycoords='axes fraction')
    plt.show()


def sample_times(times, num_examples):
    '''Assumes times is a list of floats representing finishing
    times of all runners. num_examples is an int
    Generates a random sample of size num_examples, and produces
    a histogram showing the distribution along with its mean and
    standard deviation'''
    sample = random.sample(times, num_examples)
    make_hist(sample, 10, 'Sample of Size ' + str(num_examples),
              'Minutes to Complete Race', 'Number of Runners')


def gaussian(x, mu, sigma):
    factor1 = (1/(sigma*((2*np.pi)**0.5)))
    factor2 = np.e**-(((x-mu)**2)/(2*sigma**2))
    return factor1*factor2


def test_samples(num_trials, sample_size):
    tight_means, wide_means = [], []
    for t in range(num_trials):
        smaple_tight, sample_wide = [], []
        for i in range(sample_size):
            smaple_tight.append(random.gauss(0, 1))
            sample_wide.append(random.gauss(0, 100))
        tight_means.append(sum(smaple_tight)/len(smaple_tight))
        wide_means.append(sum(sample_wide)/len(sample_wide))
    return tight_means, wide_means


tight_means, wide_means = test_samples(1000, 40)
plt.plot(wide_means, 'y*', label='SD = 100')
plt.plot(tight_means, 'bo', label='SD = 1')
plt.xlabel('Sample Number')
plt.ylabel('Sample Mean')
plt.title('Means of Samples of Size ' + str(40))
plt.legend()

plt.figure()
plt.hist(wide_means, bins=20, label='SD = 100')
plt.title('Distribution of Sample Means')
plt.xlabel('Sample Mean')
plt.ylabel('Frequency of Occurrence')
plt.legend()
plt.show()

# area = round(integrate.quad(gaussian, -3, 3, (0, 1))[0], 4)
# print('Probability of being within 3',
#       'of true mean of tight dist. =', area)
# area = round(integrate.quad(gaussian, -3, 3, (0, 100))[0], 4)
# print('Probability of being within 3',
#       'of true mean of tight dist. =', area)


# times = get_BM_data('bm_results2012.csv')['time']
# # make_hist(times, 20, '2012 Boston Marathon',
# #           'Minutes to Complete Race', 'Number of Runners')
# sample_size = 40
# sample_times(times, sample_size)
