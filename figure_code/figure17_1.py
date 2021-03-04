import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate


def roll_die():
    '''Returns a random int between 1 and 6'''
    return random.choice([1, 2, 3, 4, 5, 6])


def roll_n(n):
    result = ''
    for i in range(n):
        result += str(roll_die())
    print(result)

roll_n(10)
