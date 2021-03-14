def compare_animals(animals, precision):
    '''Assumes animals is a list of animals, precision an int >= 0
    Builds a table of distances between each animal'''
    # Get labels for columns and rows
    column_labels = [a.get_name() for a in animals]
    row_labels = column_labels[:]
    table_vals = []
    # Get distances between pairs of animals
    # For each row
    for a1 in animals:
        row = []
        # For each column
        for a2 in animals:
            distance = a1.distance(a2)
            row.append(str(round(distance, precision)))
        table_vals.append(row)
    # Produce table
    table = plt.table(rowLabels=row_labels,
                      colLabels=column_labels,
                      cellText=table_vals,
                      cellLoc='center',
                      loc='center',
                      colWidths=[0.2]*len(animals))
    plt.axis('off')
    table.scale(1, 2.5)
