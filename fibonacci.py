def fibo(n):
	print(n)
	if n <= 0:
		return 1
	fib = [0]*n
	fib[0] = 1
	fib[1] = 1
	for i in range(2,n):
		fib[i] = fib[i-1] + fib[i-2]
		print(fib[i])
	print(fib)

if __name__ == '__main__':
	fibo(6)