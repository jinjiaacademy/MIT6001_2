'''
What is the asymptotic complexity of each of the following functions?
'''


def g(L, e):
    '''L a list of ints, e is an int'''
    for i in range(100):
        for e1 in L:
            if e1 == e:
                return True
    return False


'''Answer: 100 * len(L)'''


def h(L, e):
    '''L a list of ints, e is an int'''
    for i in range(e):
        for e1 in L:
            if e1 == e:
                return True
    return False

'''Answer: e * len(L)
