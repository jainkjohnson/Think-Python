import math

def factorial(n):
	if n == 0:
		return 1
	else:
		result = factorial(n-1)
		res = n * result
		return res



def estimate_pi():
	factor = 2 * math.sqrt(2) / 9801
	k = 0
	tot = 0
	while True:
		num = factorial(4 * k) * (1103 + 26390 * k)
		den = factorial(4) ** 4 * 396 ** (4 * k)
		total = factor * ( num / den )
		tot = tot + total


		if abs(total) < 1e-15:
			break
		k = k + 1

	return 1 / tot


print estimate_pi() 				
