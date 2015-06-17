a = input()
b = input()
c = input()

def is_triangle(a, b, c):
	if ( a + b < c ):
		print "Not triangle"
	elif ( a + c < b):
		print "Not triangle"

	elif ( b + c < a ):
		print "Not triangle"

	else:
		print "Yes traingle"

is_triangle(a, b, c)
