def factorialRecursion(n):

	if n == 1:
		return 1
	else:
		return n*factorialRecursion(n-1)

print factorialRecursion(5)