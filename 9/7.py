def is_triple(word):
	i = 0
	count = 0
	while i < len(word)-1: 
		if( word[i] == word[i+1] ):
			count = count + 1
			if count == 3:
				return True
	 		i = i + 2	
		
		else:
			i = i + 1
			count = 0
	return False



def check_triple():
	fin = open('text.txt')
	for line in fin:
		word = line.strip()
		if is_triple(word):
			print word


check_triple()
