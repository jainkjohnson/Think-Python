a = input()
b = input()
c = input()
n = input()    
def check_fermat(a, b, c, n):
	
	if ( n >= 2 and a>0 and b>0 and c>0 ):
		
		if( a**n + b**n == c**n ):
			print "Holy smokes, Fermat was wrong!"	
		else: 
			print "No, that doesn't work"

check_fermat(a, b, c, n)
