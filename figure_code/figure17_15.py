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
