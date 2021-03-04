def trace_walk(drunk_kinds, num_steps):
    style_choice = style_iterator(('k+', 'r^', 'mo'))
    f = Field()
    for d_class in drunk_kinds:
        d = d_class()
        f.add_drunk(d, Location(0, 0))
        locs = []
        for s in range(num_steps):
            f.move_drunk(d)
            locs.append(f.get_loc(d))
        x_vals, y_vals = [], []
        for loc in locs:
            x_vals.append(loc.get_x())
            y_vals.append(loc.get_y())
        cur_style = style_choice.next_style()
        plt.plot(x_vals, y_vals, cur_style,
                 label=d_class.__name__)
    plt.title('Spots Visited on Walk ('
              + str(num_steps) + ' steps)')
    plt.xlabel('Steps East/West of Origin')
    plt.ylabel('Steps North/South of Origin')
    plt.legend(loc='best')
    plt.show()
