import numpy as np
import matplotlib.pyplot as plt
import scipy

t_stat = -2.26  # t-statistic for PED-X example
t_dist = []
num_bins = 1000
for i in range(10000000):
    t_dist.append(scipy.random.standard_t(198))
plt.hist(t_dist, bins=num_bins,
         weights=np.array(len(t_dist)*[1.0])/len(t_dist))
plt.axvline(t_stat, color='w')
plt.axvline(-t_stat, color='w')
plt.title('T-distribution with 198 Degrees of Freedom')
plt.xlabel('T-statistic')
plt.ylabel('Probability')
plt.show()
