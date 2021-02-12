'''
What would have to be changed to make the code in figure 3-5 work for finding an approximation
to the cube root of both negative and positive numbers?
Hint: think about changing low to ensure that the answer lies within the region being searched
'''
x = float(input('Enter an integer: '))
epsilon = 0.01
num_guesses, low = 0, 0
high = max(1, x)
ans = (high + low) / 2
while abs(ans**2 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    num_guesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2
print('number of guesses =', num_guesses)
print(ans, 'is close to square root of', x)
