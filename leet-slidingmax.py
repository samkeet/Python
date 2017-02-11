# [1,3,-1,-3,5,3,6,7]


def slideMax(nums, k):
    arrlen = len(nums)
    if arrlen == 0:
        return []
    res = []
    start, end = 0, k-1
    mx = start
    i = start
    while end < arrlen:
        if nums[i] > nums[mx]:
            mx = i
        if i == end:
            res.append(nums[mx])
            start += 1
            end += 1
            if start <= mx <= end:
                i = end
            else:
                mx = start	
                i = start
        else:
            i += 1
    return res

print(slideMax([1,3,-1,-3,5,3,6,7], 3))
print(slideMax([1,-1], 1))