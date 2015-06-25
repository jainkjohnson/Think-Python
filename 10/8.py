def has_duplicates(i):
	t = i
	t.sort()
	for item in range(len(t)-1):
		if i[item] == i[item+1]:
			return True
		return False

print has_duplicates([1,2,3,4])
print has_duplicates([1,2,2,1])
	
