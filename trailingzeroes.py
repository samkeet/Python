import math

def trailingzeroes(n):
	zero = 0
	while n > 1:
		zero += math.floor(n/(5))
		n = math.floor(n/(5))
	return zero

print(trailingzeroes(2))