class Node:
	def __init__(self, val = None):
		self.left = None
		self.right = None
		self.val = val


def lcaBST(node, a, b):
	''' Lowest Common Ancestor for
		Binary Search Tree
	'''
	if node is None:
		return node
	elif a < node.val:
		if b >= node.val:
			return node
		else:
			return lca(node.left, a, b)
	else:
		if b < node.val:
			return node
		else:
			return lca(node.right, a, b)


def lcaBinTree(node, a, b):
	''' Lowest Common Ancestor for
		Binary Tree
	'''
	if node is None:
		return node

	if node.val == a or node.val == b:
		return node
	left = lcaBinTree(node.left, a, b)
	right = lcaBinTree(node.right, a, b)
	if left and right:
		return node
	return left if left is not None else right


if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.left = Node(6)
	root.right.right = Node(7)
	print(lcaBST(root).val)
	print(lcaBinTree(root).val)