'''
Write a program that examines three variables - x, y and z - and prints the largest odd number
among them. If none of them are odd, it should print the smallest value of the three. 
'''
def largeOdd(x, y, z):
	'''Return the largest odd number among x, y and z, if none are odd,
	return the smallest value of the three.
	'''
	answer = min(x, y, z)
	if x % 2 != 0:
		answer = x
	if y % 2 != 0 and y > answer:
		answer = y
	if z % 2 != 0 and z > answer:
		answer = z
	return answer

def main():
	x = int(input('Enter a number x: '))
	y = int(input('Enter a number y: '))
	z = int(input('Enter a number z: '))
	if x % 2 != 0 or y % 2 != 0 or z % 2 != 0:
		print(f'The largest odd number is {largeOdd(x, y, z)}')
	else:
		print(f'None of them are odd, the smallest value is {largeOdd(x, y, z)}')

if __name__ == '__main__':
	main()