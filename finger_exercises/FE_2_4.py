'''
Write a program that asks the user to input 10 integers, and then 
prints the largest odd number that was entered. If no odd number was entered,
it should print a message to that effect.
'''
num_input = 1
num = int(input(f'Enter number {num_input}: '))

while num_input < 10:
    num_input += 1
    num_new = int(input(f'Enter number {num_input}: '))
    if num_new % 2 != 0 and num_new > num:
        num = num_new

if num % 2 == 0:
    print(f'None of numbers are odd.')
else:
    print(f'The largest odd number that was entered is {num}')
