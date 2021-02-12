# Test if an int > 2 is prime. If not, print smallest divisor
x = int(input('Enter an integer greater than 2: '))
smallest_divisor = None
for guess in range(2, x):
    if x % guess == 0:
        smallest_divisor = guess
        break
if smallest_divisor != None:
    print(f'Smallest divisor of {x} is {smallest_divisor}')
else:
    print(f'{x} is a prime number.')
