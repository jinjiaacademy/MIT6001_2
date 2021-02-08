# Newton-Raphson for square root
# Find x such that x**2 - 24 is within epsilon of 0
k = int(input('Enter an integer to calculate its square root: '))
epsilon = 0.01
guess = k/2
while abs(guess**2 - k) >= epsilon:
	guess = guess - (((guess**2) - k)/(2 * guess))
print('Square root of', k, 'is about', guess)