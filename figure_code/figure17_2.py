import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate


def flip(num_flips):
    '''Assumes num_flips a positive int'''
    heads = 0
    for i in range(num_flips):
        if random.choice(('H', 'T')) == 'H':
            heads += 1
    return heads / num_flips


def flip_sim(num_flips_per_trial, num_trials):
    '''Assumes num_flips_per_trial and num_trials positive ints'''
    frac_heads = []
    for i in range(num_trials):
        frac_heads.append(flip(num_flips_per_trial))
    mean = sum(frac_heads)/len(frac_heads)
    return mean


def regress_to_mean(num_flips, num_trials):
    # Get fraction of heads for each trial of num_flips
    frac_heads = []
    for t in range(num_trials):
        frac_heads.append(flip(num_flips))
    # Find trials with extreme results and for each the next trial
    extremes, next_trials = [], []
    for i in range(len(frac_heads) - 1):
        if frac_heads[i] < 0.33 or frac_heads[i] > 0.66:
            extremes.append(frac_heads[i])
            next_trials.append(frac_heads[i+1])
    # Plot results
    plt.plot(range(len(extremes)), extremes, 'ko',
             label='Extreme')
    plt.plot(range(len(next_trials)), next_trials, 'k^',
             label='Next Trial')
    plt.axhline(0.5)
    plt.ylim(0, 1)
    plt.xlim(-1, len(extremes) + 1)
    plt.xlabel('Extreme Example and Next Trial')
    plt.ylabel('Fraction Heads')
    plt.title('Regression to the Mean')
    plt.legend(loc='best')
    plt.show()


def flip_plot(min_exp, max_exp):
    '''Assumes min_exp and max_exp positive ints; min_exp < max_exp
    Plots results of 2**min_exp to 2**max_exp coin flips'''
    ratios, diffs, xAxis = [], [], []
    for exp in range(min_exp, max_exp + 1):
        xAxis.append(2**exp)
    for num_flips in xAxis:
        num_heads = 0
        for n in range(num_flips):
            if random.choice(('H', 'T')) == 'H':
                num_heads += 1
        num_tails = num_flips - num_heads
        try:
            ratios.append(num_heads/num_tails)
            diffs.append(abs(num_heads-num_tails))
        except ZeroDivisionError:
            continue
    plt.title('Difference Between Heads and Tails')
    plt.xlabel('Number of Flips')
    plt.ylabel('Abs(#Heads - #Tails)')
    plt.xticks(rotation='vertical')
    plt.plot(xAxis, diffs, 'ko')
    plt.figure()
    plt.title('Heads/Tails Ratios')
    plt.xlabel('Number of Flips')
    plt.ylabel('#Heads / #Tails')
    plt.xticks(rotation='vertical')
    plt.plot(xAxis, ratios, 'ko')
    plt.show()


def variance(X):
    '''Assumes that X is a list of numbers.
    Returns the variance of X'''
    mean = sum(X)/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return tot/len(X)


def std_dev(X):
    '''Assumes that X is a list of numbers.
    Returns the standard deviation of X'''
    return variance(X)**0.5


def CV(X):
    mean = sum(X)/len(X)
    try:
        return std_dev(X)/mean
    except ZeroDivisionError:
        return float('nan')


def make_plot(x_vals, y_vals, title, x_label, y_label, style,
              log_x=False, log_y=False):
    plt.figure()
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(x_vals, y_vals, style)
    if log_x:
        plt.semilogx()
    if log_y:
        plt.semilogx()
    plt.show()


def run_trial(num_flips):
    num_heads = 0
    for n in range(num_flips):
        if random.choice(('H', 'T')) == 'H':
            num_heads += 1
    num_tails = num_flips - num_heads
    return (num_heads, num_tails)


def flip_plot1(min_exp, max_exp, num_trials):
    '''Assumes min_exp, max_exp, num_trials ints > 0; min_exp < max_exp
    Plots summaries of results of num_trials trials of
    2**min_exp to 2**max_exp coin flips'''
    ratios_means, diffs_means, ratios_SDs, diffs_SDs = [], [], [], []
    x_axis = []
    for exp in range(min_exp, max_exp+1):
        x_axis.append(2**exp)
    for num_flips in x_axis:
        ratios, diffs = [], []
        for t in range(num_trials):
            num_heads, num_tails = run_trial(num_flips)
            ratios.append(num_heads/num_tails)
            diffs.append(abs(num_heads-num_tails))
        ratios_means.append(sum(ratios)/num_trials)
        diffs_means.append(sum(diffs)/num_trials)
        ratios_SDs.append(std_dev(ratios))
        diffs_SDs.append(std_dev(diffs))
    title = f'Mean Heads/Tails Ratios ({num_trials} Trails)'
    make_plot(x_axis, ratios_means, title, 'Number of Flips',
              'Mean Heads/Tails', 'ko', log_x=True)
    title = f'SD Heads/Tails Ratios ({num_trials} Trials)'
    make_plot(x_axis, ratios_SDs, title, 'Number of Flips',
              'Standard Deviation', 'ko', log_x=True, log_y=True)
    title = f'Mean abs(#Heads - #Tails) ({num_trials} Trails)'
    make_plot(x_axis, diffs_means, title,
              'Number of Flips', 'Mean abs(#Heads - #Tails)', 'ko',
              log_x=True, log_y=True)
    title = f'SD abs(#Heads - #Tails) ({num_trials} Trials)'
    make_plot(x_axis, diffs_SDs, title,
              'Number of Flips', 'Standard Deviation', 'ko',
              log_x=True, log_y=True)


def flip_plot2(min_exp, max_exp, num_trials):
    '''Assumes min_exp, max_exp, num_trials ints > 0; min_exp < max_exp
    num_trials a positive integer
    Plots summaries of results of num_trials trials of
    2**min_exp to 2**max_exp coin flips'''
    ratios_means, diffs_means, ratios_SDs, diffs_SDs = [], [], [], []
    ratios_CVs, diffs_CVs, x_axis = [], [], []
    for exp in range(min_exp, max_exp+1):
        x_axis.append(2**exp)
    for num_flips in x_axis:
        ratios, diffs = [], []
        for t in range(num_trials):
            num_heads, num_tails = run_trial(num_flips)
            ratios.append(num_heads/num_tails)
            diffs.append(abs(num_heads-num_tails))
        ratios_means.append(sum(ratios)/num_trials)
        diffs_means.append(sum(diffs)/num_trials)
        ratios_SDs.append(std_dev(ratios))
        diffs_SDs.append(std_dev(diffs))
        ratios_CVs.append(CV(ratios))
        diffs_CVs.append(CV(diffs))
    num_trials_str = ' (' + str(num_trials) + ' Trials)'
    title = f'Mean Heads/Tails Ratios (' + str(num_trials) + ' Trails)'
    make_plot(x_axis, ratios_means, title, 'Number of Flips',
              'Mean Heads/Tails', 'ko', log_x=True)
    title = 'SD Heads/Tails Ratios' + num_trials_str
    make_plot(x_axis, ratios_SDs, title, 'Number of Flips',
              'Standard Deviation', 'ko', log_x=True, log_y=True)
    title = 'Mean abs(#Heads - #Tails)' + num_trials_str
    make_plot(x_axis, diffs_means, title,
              'Number of Flips', 'Mean abs(#Heads - #Tails)', 'ko',
              log_x=True, log_y=True)
    title = 'SD abs(#Heads - #Tails)' + num_trials_str
    make_plot(x_axis, diffs_SDs, title,
              'Number of Flips', 'Standard Deviation', 'ko',
              log_x=True, log_y=True)
    title = 'Coeff. of Var. abs(#Heads - #Tails)' + num_trials_str
    make_plot(x_axis, diffs_CVs, title,
              'Number of Flips', 'Coeff. of Var.', 'ko',
              log_x=True)
    title = 'Coeff. of Var. Heads/Tails Ratio' + num_trials_str
    make_plot(x_axis, ratios_CVs, title,
              'Number of Flips', 'Coeff. of Var.', 'ko',
              log_x=True, log_y=True)


def flip(num_flips):
    '''Assumes num_flips a positive int'''
    heads = 0
    for i in range(num_flips):
        if random.choice(('H', 'T')) == 'H':
            heads += 1
    return heads/float(num_flips)


def flip_sim(num_flips_per_trial, num_trials):
    frac_heads = []
    for i in range(num_trials):
        frac_heads.append(flip(num_flips_per_trial))
    mean = sum(frac_heads)/len(frac_heads)
    sd = std_dev(frac_heads)
    return (frac_heads, mean, sd)


def label_plot(num_flips, num_trials, mean, sd):
    plt.title(str(num_trials) + ' trials of '
              + str(num_flips) + ' flips each')
    plt.xlabel('Fraction of Heads')
    plt.ylabel('Number of Trials')
    plt.annotate('Mean = ' + str(round(mean, 4))
                 + '\nSD = ' + str(round(sd, 4)), size='x-large',
                 xycoords='axes fraction', xy=(0.67, 0.5))


def make_plots(num_flips1, num_flips2, num_trials):
    val1, mean1, sd1 = flip_sim(num_flips1, num_trials)
    plt.hist(val1, bins=20)
    x_min, x_max = plt.xlim()
    label_plot(num_flips1, num_trials, mean1, sd1)
    plt.figure()
    val2, mean2, sd2 = flip_sim(num_flips2, num_trials)
    plt.hist(val2, bins=20, ec='k')
    plt.xlim(x_min, x_max)
    label_plot(num_flips2, num_trials, mean2, sd2)
    plt.show()


# print('Mean =', flip_sim(100, 10000))
# regress_to_mean(15, 50)
# random.seed(0)
# flip_plot(4, 20)
# flip_plot2(4, 20, 20)
make_plots(100, 1000, 10000)
