def get_final_locs(num_steps, num_trials, d_class):
    locs = []
    d = d_class()
    for t in range(num_trials):
        f = Field()
        f.add_drunk(d, Location(0, 0))
        for s in range(num_steps):
            f.move_drunk(d)
        locs.append(f.get_loc(d))
    return locs


def plot_locs(drunk_kinds, num_steps, num_trials):
    style_choice = style_iterator(('k+', 'r^', 'mo'))
    for d_class in drunk_kinds:
        locs = get_final_locs(num_steps, num_trials, d_class)
        x_vals, y_vals = [], []
        for loc in locs:
            x_vals.append(loc.get_x())
            y_vals.append(loc.get_y())
        meanX = sum(x_vals)/len(x_vals)
        meanY = sum(x_vals)/len(y_vals)
        cur_style = style_choice.next_style()
        plt.plot(x_vals, y_vals, cur_style,
                 label=(f'{d_class.__name__} mean loc. = <' +
                        f'{meanX}, {meanY}>'))
    plt.title(f'Location at End of Walks ({num_steps} steps)')
    plt.xlabel('Steps East/West of Origin')
    plt.ylabel('Steps North/South of Origin')
    plt.legend(loc='best')
    plt.show()
