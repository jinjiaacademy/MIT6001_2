def square_root_bi(x, epsilon):
    '''Assumes x and epsilon are positive floats & epsilon < 1
    Returns a y such that y*y is within epsilon of x'''
    low = 0.0
    high = max(1.0, x)
    ans = (high + low) / 2.0
    while abs(ans**2 - x) >= epsilon:
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return ans
