# Find square root of x1
if x1 < 0:
	print('Does not exist.')
else:
	low = 0
	high = max(1, x1)
	ans = (high + low) / 2
	while abs(ans**2 - x1) >= epsilon:
		if ans**2 < x1:
			low = ans
		else:
			high = ans
		ans = (high + low) / 2

x1_root = ans
x2 = -8
# Find cube root of x2
if x2 < 0:
	is_pos = False
	x2 = -x2
else:
	is_pos = True 
low = 0
high = max(1, x2)
ans = (high + low) / 2
while abs(ans**3 - x2) >= epsilon:
	if ans**3 < x2:
		low = ans
	else:
		high = ans
	ans = (high + low) / 2
if is_pos:
	x2_root = ans
else:
	x2_root = -ans
	x2 = -x2
print('Sum of square root of', x1, 'and cube root of', x2,
	'is close to', x1_root + x2_root)
