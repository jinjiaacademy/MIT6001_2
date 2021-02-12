''' 
Use find to implement a function satisfying the specification
'''


def find_last(s, sub):
    '''s and sub are non-empty strings,
    Returns the index of the last occurrence of sub in s.
    Returns None if sub does not occur in s'''
    if s.find(sub) == -1:
        return None
    return s.rfind(sub)


print(find_last('jinjia', 'i'))
print(find_last('jinjia', 'j'))
print(find_last('jinjia', 'haha'))
