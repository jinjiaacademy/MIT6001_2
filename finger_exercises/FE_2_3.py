'''
Replace the comment in the following code with a while loop
'''
num_x = int(input('How many times should I print the letter X: '))
to_print = ''
# concatenate X to to_print num_x times
while num_x > 0:
	to_print += 'X'
	num_x -= 1
print(to_print)