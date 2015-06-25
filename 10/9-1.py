def remove_duplicates(i):
	res = []
	for item in i:
		if item not in res:
			res.append(item)
	return res
	
print remove_duplicates([1,2,2,3,4,5,5,6])
