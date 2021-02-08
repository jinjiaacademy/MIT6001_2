def find_root(x, power, epsilon):
	# Find interval containing answer:
	if x < 0 and power%2 == 0:
		return None # Negative number has no even-powered roots
	low = min(-1, x)
	high = max(1, x)
	# Use bisection search
	ans = (high + low) / 2
	while abs(ans**power - x) >= epsilon:
		if ans**power < x:
			low = ans
		else:
			high = ans
		ans = (high + low) / 2
	return ans