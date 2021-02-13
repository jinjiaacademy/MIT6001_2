def f(x):
    '''Assumes x is an int > 0'''
    ans = 0
    # Loop that takes constant time
    for i in range(1000):
        ans += 1
    print('Number of additions so far', ans)
    # Loop that takes time x
    for i in range(x):
        ans += 1
    print('Number of additions so far', ans)
    # Nested loops take time x**2
    for i in range(x):
        for j in range(x):
            ans += 1
            ans += 1
    print('Number of additions so far', ans)
    return ans


print(f(10))
print(f(1000))
