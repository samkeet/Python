import itertools


def main():
    arr = [5, 4, 2, 3]
    num_list = []
    for tup in set(itertools.permutations(arr)):
        num_list.append(int(''.join(str(x) for x in tup)))
    num_list.sort()
    val = 0
    for i in num_list:
        if i < 2400:
            val = str(i)
        else:
            break
    print(val[:2]+":"+val[2:])


def inversion(arr):
    x = 0
    y = len(arr)-1
    for i in range(len(arr)):
        if arr[i] > arr[i+1]:
            x = i
            break

    for j in range(len(arr)-1, -1, -1):
        if arr[j] < arr[j-1]:
            y = j
            break
    mx = arr[x]
    mn = arr[y]
    for i in range(x+1, y+1):
        if arr[i] > mx:
            mx = arr[i]
        if arr[i] < mn:
            mn = arr[i]

    for i in range(0, x):
        if arr[i] < mn:
            x = i

    for i in range(len(arr)-1, y-1, -1):
        if arr[i] > mx:
            y = i

    print(y-x+1)


main()


inversion([10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60])
