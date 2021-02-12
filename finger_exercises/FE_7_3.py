'''
Write a program that first stores the first ten numbers in the 
Fibonnaci sequence to a file name fib_file. Each number should be
on a seperate line in the file. The program should then read the
numbers from the file and print them.
'''


def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


with open('fib_file', 'w') as f:
    for i in range(10):
        f.write(f'{fib(i)}\n')

with open('fib_file', 'r') as f:
    for line in f:
        print(line[:-1])
