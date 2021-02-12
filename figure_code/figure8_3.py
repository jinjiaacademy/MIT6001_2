def is_pal(x):
    '''Assumes x is a list
    Returns True if the list is a palindrome; False otherwise'''
    temp = x[:]
    temp.reverse()
    return temp == x


def silly(n):
    '''Assumes n is an int > 0
    Gets n inputs from user
    Prints 'Yes' if the sequence of inputs forms a palindrome;
    'No' otherwise'''
    result = []
    for i in range(n):
        elem = input('Enter elements: ')
        result.append(elem)
    if is_pal(result):
        print('Yes')
    else:
        print('No')
