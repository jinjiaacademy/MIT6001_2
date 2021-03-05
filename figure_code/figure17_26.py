import random
import numpy as np
import scipy.integrate


def gaussian(x, mu, sigma):
    '''Assumes x, mu, sigma numbers
    Returns the value of P(x) for a Gaussian
    with mean mu and sd sigma'''
    factor1 = (1.0/(sigma*((2*np.pi)**0.5)))
    factor2 = np.e**-(((x-mu)**2)/(2*sigma**2))
    return factor1*factor2


def check_empirical(mu_max, sigma_max, num_trials):
    '''Assumes mu_max, sigma_max, num_trials positive ints
    prints fraction of values of a Gaussians (with randomly
    chosen mu and sigma) falling within 1, 2, 3 standard
    deviations'''
    for t in range(num_trials):
        mu = random.randint(-mu_max, mu_max+1)
        sigma = random.randint(1, sigma_max)
        print('For mu =', mu, 'and sigma =', sigma)
        for num_std in (1, 2, 3):
            area = scipy.integrate.quad(gaussian, mu-num_std*sigma,
                                        mu+num_std*sigma,
                                        (mu, sigma))[0]
            print(' Fraction within', num_std, 'std =',
                  round(area, 4))


check_empirical(10, 10, 3)
