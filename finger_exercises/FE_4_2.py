'''
Write a function is_in that accepts two strings as arguments and returns
True if either string occurs anywhere in the other, and False otherwise.
Hint: you might want to use the built-in str operator in
'''


def is_in(str1, str2):
    if str1 in str2 or str2 in str1:
        return True
    else:
        return False
