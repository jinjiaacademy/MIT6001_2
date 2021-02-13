def f(i):
    '''Assumes i is an int and i >= 0'''
    answer = 1
    while i >= 1:
        answer *= i
        i -= 1
    return answer


def linear_search(L, x):
    for e in L:
        if e == x:
            return True
    return False


def fact(n):
    '''Assumes n is a positive int
    Returns n!'''
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer
