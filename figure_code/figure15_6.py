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
