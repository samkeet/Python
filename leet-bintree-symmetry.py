# O(nlog n + n)
def getLists(node, l, level):
    if node is None:
        return
    if len(l) == level:
        ls = []
    else:
        ls = l[level]
    ls.append(node.val)
    ls = getLists(node.left, ls, level+1)
    ls = getLists(node.right, ls, level+1)
    return ls

def binTreeSymmetry(node):

    if node is None:
        return []
    l = getLists(node,[],0)

    # check for palindrome in each list
    for i in range(len(l))
    ls = l[i]
    llen = len(ls)
    j = 0
    for i in range(len(ls)/2, -1, -1):
        if ls[i] != ls[len(ls)/2+j]:
            return False
        j += 1
    
