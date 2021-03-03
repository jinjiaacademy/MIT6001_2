# -*- coding: utf-8 -*-

# # Figure 14-2 from page 284
class Item(object):
    def __init__(self, n, v, w):
        self._name = n
        self._value = v
        self._weight = w

    def get_name(self):
        return self._name

    def get_value(self):
        return self._value

    def get_weight(self):
        return self._weight

    def __str__(self):
        return f'<{self._name}, {self._value}, {self._weight}>'


def value(item):
    return item.get_value()


def weight_inverse(item):
    return 1.0/item.get_weight()


def density(item):
    return item.get_value()/item.get_weight()


def max_val(to_consider, avail):
    '''Assumes to_consider a list of items, avail a weight
    Returns a tuple of the total value of a solution to the
    0/1 knapsack problem and the items of that solution'''
    if to_consider == [] or avail == 0:
        result = (0, ())
    elif to_consider[0].get_weight() > avail:
        # Explore right branch only
        result = max_val(to_consider[1:], avail)
    else:
        next_item = to_consider[0]
        # Explore left branch
        with_val, with_to_take = max_val(to_consider[1:],
                                         avail-next_item.get_weight())
        with_val += next_item.get_value()
        # Explore right branch
        without_val, without_to_take = max_val(to_consider[1:], avail)
        # Choose better branch
        if with_val > without_val:
            result = (with_val, with_to_take + (next_item,))
        else:
            result = (without_val, without_to_take)
    return result


def small_test():
    names = ['a', 'b', 'c', 'd']
    vals = [6, 7, 8, 9]
    weights = [3, 3, 2, 5]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    val, taken = max_val(Items, 5)
    for item in taken:
        print(item)
    print('Total value of items taken =', val)


def build_many_items(num_items, max_val, max_weight):
    items = []
    for i in range(num_items):
        items.append(Item(str(i),
                          random.randint(1, max_val),
                          random.randint(1, max_weight)))
    return items


def big_test(num_items, avail_weight):
    items = build_many_items(num_items, 10, 10)
    val, taken = max_val(items, avail_weight)
    print('Items Taken')
    for item in taken:
        print(item)
    print('Total value of items taken =', val)

small_test()
