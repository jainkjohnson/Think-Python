def is_reverse(x, y):
	if len(x) != len(y):
		return False
	i = 0;
	j = len(y)
	j = j - 1
 	while j != 0:
		if x[i] != y[j]:
			return False
		i = i + 1
		j = j - 1
	return True

print is_reverse('stop','pots')

