def get_ratio(vect1, vect2):
    '''Assumes: vect1 and vect2 are equal length lists of numbers
    Returns: a list containing the meaningful values of
            vect1[i]/vect2[i]'''

    ratio = []
    for index in range(len(vect1)):
        try:

            ratio.append(vect1[index]/vect2[index])
        except ZeroDivisionError:
            ratio.append(float('nan'))  # nan = not a number
        except:
            raise ValueError('get_ratio called with bad arguments')
    return ratio


try:
    print(get_ratio([1, 2, 7, 6], [1, 2, 0, 3]))
    print(get_ratio([], []))
    print(get_ratio([1, 2], [3]))
except ValueError as msg:
    print(msg)
