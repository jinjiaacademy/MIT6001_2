def sim_drunk(num_trials, d_class, walk_lengths):
    meanDistances = []
    for num_steps in walk_lengths:
        print('Starting simulation of', num_steps, 'steps')
        trials = sim_walks(num_steps, num_trials, d_class)
        mean = sum(trials)/len(trials)
        meanDistances.append(mean)
    return meanDistances


def sim_all_plot(drunk_kinds, walk_lengths, num_trials):
    style_choice = style_iterator(('m-', 'r:', 'k-.'))
    for d_class in drunk_kinds:
        cur_style = style_choice.next_style()
        print('Starting simulation of', d_class.__name__)
        means = sim_drunk(num_trials, d_class, walk_lengths)
        plt.plot(walk_lengths, means, cur_style,
                 label=d_class.__name__)
    plt.title(f'Mean Distance from Origin ({num_trials} trials)')
    plt.xlabel('Number of Steps')
    plt.ylabel('Distance from Origin')
    plt.legend(loc='best')
    plt.semilogx()
    plt.semilogy()
