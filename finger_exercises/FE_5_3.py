'''
Write a list comprehension that generates all non-primes 
between 2 and 100
'''
# nonPrimes = []
# for x in range(2, 100):
# 	for y in range(3, x):
# 		if x % y == 0:
# 			nonPrimes.append(x)
# 			break
# print(nonPrimes)

nonPrimes = [x for x in range(2, 100) if any(x%y == 0 for y in range(3, x))]
print(nonPrimes)