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
