def palindrome(i, start, length):
	
	rev = str(i)[start:start+length]
	
	return rev[::-1] == rev


def condition(i):

	return( palindrome(i, 2, 4) and 
	    	palindrome(i+1, 1, 5) and
	   	palindrome(i+2, 1, 4) and
	   	palindrome(i+3, 0, 6))
	   


def check():
	i = 100000
	while i <= 999999:
		
		if condition(i):
			print "the number ",i
		i = i + 1


check()
print
		
