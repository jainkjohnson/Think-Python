def cumulative_sum(i):
	res = []
	total = 0
	for item in i:
		total += item
		res.append(total)
	return res
print cumulative_sum([1,2,3])
