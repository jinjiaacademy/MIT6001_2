def fast_max_val(to_consider, avail, memo={}):
    '''Assumes to_consider a list of items, avail a weight
    memo supplied by recursive calls
    Returns a tuple of the total value of a solution to the
    0/1 knapsack problem and the items of that solution'''
    if (len(to_consider), avail) in memo:
        result = memo[(len(to_consider), avail)]
    elif to_consider == [] or avail == 0:
        result = (0, ())
    elif to_consider[0].get_weight() > avail:
        # Explore right branch only
        result = fast_max_val(to_consider[1:], avail, memo)
    else:
        next_item = to_consider[0]
        # Explore left branch
        with_val, with_to_take = fast_max_val(to_consider[1:],
                                              avail - next_item.get_weight(),
                                              memo)
        with_val += next_item.get_value()
        # Explore right branch
        without_val, without_to_take = fast_max_val(to_consider[1:],
                                                    avail, memo)
        # Choose better branch
        if with_val > without_val:
            result = (with_val, with_to_take + (next_item,))
        else:
            result = (without_val, without_to_take)
    memo[(len(to_consider), avail)] = result
    return result
