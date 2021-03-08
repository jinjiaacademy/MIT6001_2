import numpy as np
import matplotlib.pyplot as plt


def get_data(input_file):
    with open(input_file, 'r') as data_file:
        distances = []
        masses = []
        data_file.readline()  # ignore header
        for line in data_file:
            d, m = line.split(',')
            distances.append(float(d))
            masses.append(float(m))
    return (masses, distances)


def plot_data(input_file):
    masses, distances = get_data(input_file)
    distances = np.array(distances)
    masses = np.array(masses)
    forces = masses*9.81
    plt.plot(forces, distances, 'bo',
             label='Measured displacements')
    plt.title('Measured Displacement of Spring')
    plt.xlabel('|Force| (Newtons)')
    plt.ylabel('Distance (meters)')
    plt.show()


def fit_data(input_file):
    masses, distances = get_data(input_file)
    distances = np.array(distances[:-6])
    forces = np.array(masses[:-6])*9.81
    plt.plot(forces, distances, 'ko',
             label='Measured displacements')
    plt.title('Measured Displacement of Spring')
    plt.xlabel('|Force| (Newtons)')
    plt.ylabel('Distance (meters)')
    # find linear fit
    a, b = np.polyfit(forces, distances, 1)
    predicted_distances = a*np.array(forces) + b
    k = 1.0/a
    plt.plot(forces, predicted_distances,
             label=f'Linear fit, k = {k:.4f}')
    plt.legend(loc='best')
    # find cubic fit
    fit = np.polyfit(forces, distances, 3)
    predicted_distances = np.polyval(fit, forces)
    plt.plot(forces, predicted_distances, 'k:', label='cubic fit')
    plt.show()


# plot_data('springData.csv')
fit_data('springData.csv')
