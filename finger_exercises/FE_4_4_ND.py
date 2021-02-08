'''
Write a function mult that accepts either one or two ints
as arguments. If called with two arguments, the function prints
the product of the two arguments. If called with one argument,
it prints that argument.
'''
def mult(x, y, single=True):
	if single:
		print(x)
	else:
		print(x * y)


mult(10, 20, False)
