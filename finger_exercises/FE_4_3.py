'''
Write a function to test is_in
'''


def is_in(str1, str2):
    if str1 in str2 or str2 in str1:
        return True
    else:
        return False


def test_is_in(str1s, str2s):
    for str1 in str1s:
        for str2 in str2s:
            result = is_in(str1, str2)
            if result:
                val = True
            else:
                val = False
            print(f'{str1} - {str2} : {val}')


str1s = ['hello', 'stop', 'jinjia']
str2s = ['lo', 'sp', 'inj']
test_is_in(str1s, str2s)
