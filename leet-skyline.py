def mergeSkyline(left, right):
    # 2D array of x-coordinate, height sorted by x
    # traverse through each element and its next
    # print(left, right)
    if left is None:
        return right
    elif right is None:
        return left
    res = []
    h1, h2 = 0, 0
    i, j = 0, 0
    while i < len(left) and j < len(right):
        x = left[i]
        y = right[j]
        if x[0] < y[0]:
            h1 = x[1]
            res.append([x[0], max(h1, h2)])
            i += 1
        elif x[0] > y[0]:
            h2 = y[1]
            res.append([y[0], max(h1, h2)])
            j += 1
        else:
            h1 = x[1]
            h2 = y[1]
            res.append([x[0], max(h1, h2)])
            i += 1
            j += 1
        try:
            if res[-1][1] == res[-2][1]:
                res.pop()
        except:
            pass
    if i != len(left):
        while i != len(left):
            res.append(left[i])
            i += 1
    if j != len(right):
        while j != len(right):
            res.append(right[j])
            j += 1
    print(res)
    return res


def skyline(buildings):
    print(buildings)
    arr_len = len(buildings)
    if arr_len == 1:
        return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
    if arr_len > 1:
        left = skyline(buildings[:arr_len//2])
        right = skyline(buildings[arr_len//2:])
        res = mergeSkyline(left, right)
        return res


res = skyline([[1,2,1],[1,2,2],[1,2,3]])
print(res)
