'''
Implement a function that meets the specification below.
Use a try-except block. Hint: before starting to code, you 
might want to type something like 1 + 'a' in to the shell 
to see what kind of exception is raised.
'''
def sum_digits(s):
	'''Assumes s is a string
	Returns the sum of the decimal digits in s
	For example, if s is 'a2b3c' it returns 5'''
	try:
		type(s) == str
		total = 0
		for i in s:
			if i in '1234567890':
				total += int(i)
		return total
	except TypeError:
		print('Unsuported type, please enter a string')
	

print(sum_digits((1,)))