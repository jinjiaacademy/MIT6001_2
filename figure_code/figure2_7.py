'''
Squaring an integer, the hard way
'''
x = 3
ans = 0
num_iterations = 0
while num_iterations < abs(x):
    ans += abs(x)
    num_iterations += 1
print(f'{x} * {x} = {ans}')
