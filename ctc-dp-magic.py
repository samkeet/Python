def findMagic(arr):
	l = []
	for i in range(len(arr)):
		if arr[i] == i:
			l.append(i)