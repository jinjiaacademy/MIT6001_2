# Find approximation to square root of x 
if x < 0:
	print('Does not exist.')
else:
	low = 0
	high = max(1, x)
	ans = (high + low) / 2
	while abs(ans**2 - x) >= epsilon:
		if ans**2 < x:
			low = ans
		else:
			high = ans 
		ans = (high + low) / 2
	print(ans, 'is close to square root of', x)