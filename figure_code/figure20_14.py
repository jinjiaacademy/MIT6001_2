def get_horizontal_speed(quad_fit, min_x, max_x):
    '''Assumes quad_fit has coefficients of a quadratic polynomial
    min_x and max_x are distances in inches
    Returns horizontal speed in feet per second'''
    inches_per_foot = 12
    x_mid = (max_x - min_x)/2
    a, b, c = quad_fit[0], quad_fit[1], quad_fit[2]
    y_peak = a*x_mid**2 + b*x_mid + c
    g = 32.16*inches_per_foot
    t = (2*y_peak/g)**0.5
    print('Horizontal speed =', int(x_mid/(t*inches_per_foot)), 'feet/sec')
