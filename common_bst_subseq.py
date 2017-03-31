class Node:
	def __init__(self, val = None):
		self.left = None
		self.right = None
		self.val = val


def bstSubSeq(node, arr):
	index = 0
	arrlen = len(arr)
	if node is None or arrlen == 0:
		return False
	st = []
	while node is not None:
		st.push(node)
		node = node.left
	while not st.empty():
		while node is not None:
			st.push(node)
			node = node.left
		node = st.pop()
		if node.val == arr[index]:
			index += 1
			if index == arrlen:
				return True
		node = node.right
	return False


_index = 0

def bstSubSeq(node, arr, index):
	if node is None or len(arr) == 0:
		return
	bstSubSeq(node.left, arr, index):
	if node.val == arr[index]
		index += 1
	bstSubSeq(node.right, arr, index)