def reverseList(l):

	if len(l) == 0:
		return []
	return reverseList(l[1:]) + [l[0]]

print reverseList([1,2,3,4,5])
