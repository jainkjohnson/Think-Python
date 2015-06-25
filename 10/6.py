def is_sorted(i):
	try:
		for code,item in enumerate(i):
			if item > i[code+1]: 
				return False
	except IndexError:
		return True	
		
	

print is_sorted([1,3,2])
print is_sorted([3,2,1])
