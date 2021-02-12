def fact_iter(n):
    '''Assumes n an int > 0
    Return n!'''
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def fact_rec(n):
    '''Assumes n an int > 0
    Returns n!'''
    if n == 1:
        return n
    else:
        return n*fact_rec(n-1)
