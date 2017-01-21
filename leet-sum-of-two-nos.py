class Solution(object):
    
    def insertionSort(arr):
        N = len(arr)
        for i in range(1, N):
            j = i - 1
            temp = arr[i]
            while j >= 0 and temp < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = temp
        return arr
        
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = insertionSort(nums)
        i=0
        while i <= len(nums):
            if nums[i] > target: i += 1
            else: break
        nums = nums[i:]
        i = 0
        while i < len(nums):
            if (target - nums[i]) in nums:
                return [i,nums.index(target - nums[i])]

