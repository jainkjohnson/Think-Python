def nestedsum(i):
	total = 0
	for item in i:
		if isinstance(item, list):
			total += nestedsum(item)
		else:
			total += item

	return total


print nestedsum([1,2,[1,2]])


