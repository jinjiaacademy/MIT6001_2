def sample_times(times, num_examples):
    '''Assumes times is a list of floats representing finishing
    times of all runners. num_examples is an int
    Generates a random sample of size num_examples, and produces
    a histogram showing the distribution along with its mean and
    standard deviation'''
    sample = random.sample(times, num_examples)
    make_hist(sample, 10, 'Sample of Size ' + str(num_examples),
              'Minutes to Complete Race', 'Number of Runners')

