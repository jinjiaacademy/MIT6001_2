'''
Using the algorithm of figure 3-6, write a function that satisfies the specification
'''


def log(x, base, epsilon):
    '''Assumes x and epsilon int or float, base an int, 
            x > 1, epsilon > 0 & power >= 1
    Returns float y such that base**y is within epsion of x'''
    # Find lower bound on ans
    lower_bound = 0
    while base ** lower_bound < x:
        lower_bound += 1
    low = lower_bound - 1
    high = lower_bound + 1
    # Perform bisection search
    ans = (high + low) / 2
    while abs(base**ans - x) >= epsilon:
        if base ** ans < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return ans


a = log(100, 10, 0.01)
print(a)
