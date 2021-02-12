'''
When the implementation of fib in figure 6-3 is used to 
compute fib(5), how many times does it compute the value of fit(2)
on the way to computing fib(5)?
'''


def fib(n):
    '''Assumes n int >= 0
    Returns Fibonacci of n'''
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def test_fib(n):
    for i in range(n+1):
        print('fib of', i, '=', fib(i))


test_fib(5)

3
