def minJumps(arr):
	arrlen = len(arr)
	if arrlen <= 0:
		return -1
	res = [sys.maxint()]*arrlen
	res[arrlen-1] = 0
	for i in range(arrlen-2, -1, -1):
		max_jump = arr[i]
		min_ = sys.maxint()
		if i + max_jump >= arrlen-1:
			res[i] = 1
		else:
			for j in range(i+1, n):
				if j <= i + max_jump:
					if res[j] < min_:
						min_ = res[j]
			res[i] = min_ + 1 if min_ != sys.maxint else min_