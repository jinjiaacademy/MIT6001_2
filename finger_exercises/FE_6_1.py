'''
The harmonic sum of an integer, n > 0, can be calculated 
usint the formula
1 + 1/2 + ... + 1/n
Write a recursive function that computes this.
'''
def harmonic_sum(n):
	if n == 1:
		return n
	else:
		return (1/n) + harmonic_sum(n-1)

print(harmonic_sum(5))