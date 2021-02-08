def log(x, base, epsilon):
	'''Assumes x and epsilon int or float, base an int,
		x > 1, epsilon > 0 and power >= 1
	Returns float y such that base**y is within epsilon of x'''
	def find_log_bounds(x, base):
		upper_bound = 0
		while base**upper_bound < x:
			upper_bound += 1
		return upper_bound - 1, upper_bound
	low, high = find_log_bounds(x, base)
	return bisection_solve(x, lambda ans: base**ans, epsilon, low, high)