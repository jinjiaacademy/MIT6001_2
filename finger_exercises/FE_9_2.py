'''
Implement a function that satisfies the specification
'''


def find_an_even(L):
    '''Assumes L is a list of integers
    Returns the first even number in L
    Raises ValueError if L does not contain an even number'''
    for x in L:
        if x % 2 == 0:
            return x
    raise ValueError('No even number in L')


# print(find_an_even([1, 2, 3, 4, 5, 6]))
print(find_an_even([3, 3, 1, 1, 1, 1]))
