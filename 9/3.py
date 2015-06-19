def avoids(a,b,c,d,e):
	fin = open('text.txt')
	count = 0
	for line in fin:
		if ( a or b or c or d or e ) not in line:
		
			print line
			count = count + 1
		

	print count

		
avoids('z','y','w','d','e')



