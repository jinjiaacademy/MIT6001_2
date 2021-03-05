import random
import matplotlib.pyplot as plt

random.seed(0)
vals = []
for i in range(1000):
    num1 = random.choice(range(0, 101))
    num2 = random.choice(range(0, 101))
    vals.append(num1 + num2)
plt.hist(vals, bins=10, ec='k')
plt.xlabel('Sum')
plt.ylabel('Number of Occurrences')
plt.show()
