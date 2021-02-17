import numpy as np
import mmatplotlib.pyplot as plt

def find_payment(loan, r, m):
    '''Assumes: loan and r are floats, m an int
    Returns the monthly payment for a mortgage of size
    loan at a monthly rate of r for m months'''
    return loan*((r*(1+r)**m)/((1+r)**m-1))


class Mortgage(object):
    '''Abstract class for building different kinds of mortgages'''

    def __init__(self, loan, annRate, months):
        self._loan = loan
        self._rate = annRate/12.0
        self._months = months
        self._paid = [0.0]
        self._outstanding = [loan]
        self._payment = find_payment(loan, self._rate, months)
        self._legend = None  # description of mortgage

    def make_payment(self):
        self._paid.append(self._payment)
        reduction = self._payment - self._outstanding[-1]*self._rate
        self._outstanding.append(self._outstanding[-1] - reduction)

    def get_total_paid(self):
        return sum(self._paid)

    def __str__(self):
        return self._legend

    def plot_payments(self, style):
        plt.plot(self._paid[1:], style, label=self._legend)

    def plot_balance(self, style):
        plt.plot(self._outstanding, style, label=self._legend)

    def plot_tot_pd(self, style):
        tot_pd = [self._paid[0]]
        for i in range(1, len(self._paid)):
            tot_pd.append(tot_pd[-1] + self._paid[i])
        plt.plot(tot_pd, style, label=self._legend)

    def plot_net(self, style):
        tot_pd = [self._paid[0]]
        for i in range(1, len(self._paid)):
            tot_pd.append(tot_pd[-1] + self._paid[i])
        equity_aquired = np.array([self._loan]*len(self._outstanding))
        equity_aquired = equity_aquired - np.array(self._outstanding)
        net = np.array(tot_pd) - equity_aquired
        plt.plot(net, style, label=self._legend)
