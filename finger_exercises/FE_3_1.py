'''
Change the code in figure 3-2 so that it returns the largest
rather than the smallest divisor.
Hint: if y * z = x and y is the smallest divisor of x, z is the largest divisor of x
'''
x = int(input('Enter an integer greater than 2: '))
smallest_divisor = None
for guess in range(2, x):
	if x % guess == 0:
		smallest_divisor = guess
		break
if smallest_divisor != None:
	print(f'Largest divisor of {x} is {int(x/smallest_divisor)}')
else:
	print(f'{x} is a prime number.')