'''
Write a program that asks the user to enter an integer and prints two integers,
root and pwr, such that 1 < pwr < 6 and root ** pwr is equal to the integer entered
by the user. If no such pair of integers exists, it should print a message to that effect.
'''
x = int(input('Enter an integer: '))

result = []
for pwr in range(2, 6):
	for root in range(x):
		if root ** pwr == x:
			result.append((root, pwr))
if result:
	print(result)
else:
	print('No such pair of integers exists.')