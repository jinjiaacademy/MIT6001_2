'''
Write a lambda expression that has two numeric parameters.
If the second argument equals zero, it should return None.
Otherwise it should return the value of dividing the first argument
by the second argument. Hint: use a conditional expression
'''
def div(x, y): return x / y if y != 0 else None


print(div(5, 10))
print(div(5, 0))
