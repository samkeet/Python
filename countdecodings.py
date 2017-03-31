res = []*len(arr)
res[0] = 1
res[1] = 1

def countdecodings(arr, index):
	if index == 0:
		res[0] = 1
		return res
	count = countdecodings(arr, index+1)
	if 10 <= arr[index-1]*10 + arr[index] <= 27:
		res[index] = res[index-1]+1
		return res
	return res

if __name__ == '__main__':
	print(countdecodings([1,2,3], 2))