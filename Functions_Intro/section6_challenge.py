def sum_eo(n, t):
	summed_value = 0
	if t == 'e':
		for val in range(2, n, 2):
			summed_value += val
		return summed_value
	if t == 'o':
		for val in range(1, n, 2):
			summed_value += val
		return summed_value
	return -1


even_sum = sum_eo(10, 'e')
odd_sum = sum_eo(7, 'o')
no_sum = sum_eo(11, 'spam')

print("Even: {}, Odd: {}, Wrong: {}".format(even_sum, odd_sum, no_sum))

