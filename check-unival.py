# universal binary trees
# all values in the tree are same
def unival(node):
	if node is None:
		return True
	elif node.left is None and node.right is None:
		return None
	else:
		return checkUnival(node.left, node.val) and checkUnival(node.right, val)

def checkUnival(node, val):
	if node is None:
		return
	elif node.val == val:
		return checkUnival(node.left, val) and checkUnival(node.right, val)
	else:
		return False