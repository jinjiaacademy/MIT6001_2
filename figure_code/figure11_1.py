def square_root_exhaustive(x, epsilon):
    '''Assumes x and epsilon are positive floats & epsilon < 1
    Returns a y such that y*y is written epsilon of x'''
    step = epsilon ** 2
    ans = 0.0
    while abs(ans**2 - x) >= epsilon and ans*ans <= x:
        ans += step
    if ans*ans > x:
        raise ValueError
    return ans
