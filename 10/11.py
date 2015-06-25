def bisect(i, start, end):
	search = 10
	print start
	print end
	mid = (start + end) / 2
	if i[mid] == 10:
		print "Got it"
	elif i[mid] < 10:
		start = mid+1
		bisect(i,start,end)
	elif i[mid] > 10:
		end = mid-1
		bisect(i,start,end)
	
	else:
		print "not fount"


i = [10,20,30,150,200]

bisect(i,0,len(i))


