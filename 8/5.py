string = raw_input()
word = raw_input()

def count(string, word):
	count = 0
	for letter in string:
		if letter == word:
			count = count + 1
		
	print count

count(string, word)
