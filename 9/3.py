def avoids(a,b,c,d,e):
	fin = open('text.txt')
	count = 0
	for line in fin:
		if ( a in line or b in line or c in line or d in line or e in line):
			pass
		else:
			print line
			count = count + 1
		
	
	print count

		
avoids('z','y','w','d','e')



