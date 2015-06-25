import time

def function1():
	t = []
	fin = open('text.txt')
	for line in fin:
		t.append(line)

	return t


def function2():
	p = []
	fin = open('text.txt')
	for line in fin:
		p = p + [line]
	return p


start = time.time()
t = function1()
elapse = time.time() - start


print start
print elapse


start = time.time()
t = function2()
elapse = time.time() - start

print start
print elapse


