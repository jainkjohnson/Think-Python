def rotate_word(string, count):
	for letter in string:
		num = ord(letter)
		num = num + count
		print chr(num)
		
rotate_word('cheer', 7)	
