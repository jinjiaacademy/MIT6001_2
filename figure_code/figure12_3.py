def search(L, e):
    '''Assumes L is a list, the elements of which are in
    ascending order.
    Returns True if e is in L and False otherwise.'''

    def bin_search(L, e, low, high):
        # Decrements high - low
        if high == low:
            return L[low] == e
        mid = (high + low) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False
            else:
                return bin_search(L, e, low, mid-1)
        else:
            return bin_search(L, e, mid+1, high)

    if len(L) == 0:
        return False
    else:
        return bin_search(L, e, 0, len(L)-1)
