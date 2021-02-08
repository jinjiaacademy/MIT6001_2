'''
Implement a function that meets the specification
'''
def get_min(d):
	'''d a dict mapping letters to ints
	returns the value in d with the key that occurs first in the alphabet. 
	e.g., if d = {x:11, b:12}, get_min returns 12'''
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	for letter1 in alphabet:
		for letter2 in d.keys():
			if letter1 == letter2:
				return d[letter2]

d = {'x':11, 'b':12}
print(get_min(d))