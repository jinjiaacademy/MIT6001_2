def find_extreme_divisor(n1, n2):
    '''Assumes that n1 and n2 are positive ints
    Returns a tuple containing the smallest common divisor > 1 and 
    the largest common divisor of n1 & n2. If no common divisor other
    than 1, return (None, None)'''
    min_val, max_val = None, None
    for i in range(2, min(n1, n2)+1):
        if n1 % i == 0 and n2 % i == 0:
            if min_val == None:
                min_val = i
            max_val = i
    return min_val, max_val
