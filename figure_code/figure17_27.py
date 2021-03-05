def show_error_bars(min_exp, max_exp, num_trials):
    '''Assumes min_exp and max_exp positive ints; min_exp < max_exp
    num_trials a positive integer
    Plots mean fraction of heads with error bars'''
    means, sds, x_vals = [], [], []
    for exp in range(min_exp, max_exp+1):
        x_vals.append(2**exp)
        frac_heads, mean, sd = flip_sim(2**exp, num_trials)
        means.append(mean)
        sds.append(sd)
    plt.errorbar(x_vals, means, yerr=1.96*np.array(sds))
    plt.semilogx()
    plt.title('Mean Fraction of Heads ('
              + str(num_trials) + ' trials)')
    plt.xlabel('Number of flips per trial')
    plt.ylabel('Fraction of heads & 95% condifence')
    plt.show()
