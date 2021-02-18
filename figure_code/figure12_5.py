def merge(left, right, compare):
    '''Assumes left and right are sorted lists and
    compare defines an ordering on the elements.
    Returns a new sorted (by compare) list containing the
    same elements as (left + right) would contain.'''

    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result


def merge_sort(L, compare=lambda x, y: x < y):
    '''Assumes L is a list, compare defines an ordering
    on elements of L
    Returns a new sorted list with the same elements as L'''
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)


def last_name_first_name(name1, name2):
    arg1 = name1.split(' ')
    arg2 = name2.split(' ')
    if arg1[1] != arg2[1]:
        return arg1[1] < arg2[1]
    else:  # last names the same, sort by first name
        return arg1[0] < arg2[0]


def first_name_last_name(name1, name2):
    arg1 = name1.split(' ')
    arg2 = name2.split(' ')
    if arg1[0] != arg2[0]:
        return arg1[0] < arg2[0]
    else:  # first names the same, sort by last name
        return arg1[1] < arg2[1]


L = ['Tom Brady', 'Eric Grimson', 'Gisele Bundchen']
newL = merge_sort(L, last_name_first_name)
print('Sorted by last name =', newL)
newL = merge_sort(L, first_name_last_name)
print('Sorted by first name =', newL)
# L = [2, 1, 4, 5, 3]
# print(merge_sort(L), merge_sort(L, lambda x, y: x > y))
