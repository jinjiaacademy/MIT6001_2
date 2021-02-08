def bisection_solve(x, eval_ans, epsilon, low, high):
	'''x, epsilon, low, high are floats
	epsilon > 0
	eval_ans a function mapping a float to a float
	low <= high and there is an ans between low and high s.t.
		ans**power is within epsilon of x
	returns ans s.t. ans**power within epsilon of x'''
	ans = (high + low) / 2
	while abs(eval_ans(ans) - x) >= epsilon:
		if eval_ans(ans) < x:
			low = ans
		else:
			high = ans
		ans = (high + low) / 2
	return ans 