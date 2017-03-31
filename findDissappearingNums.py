def findDisappearedNumbers(nums):
	res = [-1]*len(nums)
	j = 0
	for i in range(len(nums)):
		res[nums[i]-1] = nums[i]
	for i in range(len(res)):
		if res[i] == -1:	
			nums[j] = i+1
			j += 1
	print(nums[:j])

if __name__ == '__main__':
	findDisappearedNumbers([4,3,2,7,8,2,3,1])