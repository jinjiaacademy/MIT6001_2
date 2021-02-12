'''
Write a program that prints the sum of the prime numbers 
greater than 2 and less than 100.
'''
total = 0

for number in range(3, 10):
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        print(number)
        total += number

print(f'Total: {total}')
