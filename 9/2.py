def has_no_e():
	fin = open('text.txt')
	for line in fin:
		if not 'e' in line:
			print line
		


has_no_e()	
