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
