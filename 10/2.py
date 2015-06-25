def capitalized_nest(i):
	res = []
	for item in i:
		if isinstance(item, list):
			res.append(capitalized_nest(item))
		else:
			res.append(item.capitalize())
	return res

print capitalized_nest(['a','b',['a','b']])
