import sys
def getRow(n):
	print(n)
	if n == 1:
		print([1])
	elif n == 2:
		print([1,2,1])
	else:
		prev = [1,2,1]	
		next = []
		for i in range(n-2):
			for j in range(len(prev)-1):
				next.append(prev[i]+prev[i+1])
			prev = [1]+next+[1]
			print(prev)
			next = []
		print(prev)

if __name__ == '__main__':
	getRow(int(sys.argv[1]))	