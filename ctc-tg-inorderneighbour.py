def getNodeObj(btree, val):

	unvisited = []
	visited = []
	unvisited.append(btree)

	while unvisited:
		node = unvisited.pop()
		if node.data == val:
			return node
		neighbours = node.getNeighbours()
		for v in neighbours:
			if v not in visited:
				unvisited.append(v)
		visited.append(node)
	return -1

def getMin(btree):

	while btree.leftChild.leftChild:
		btree = btree.leftChild
	return btree.data

def getInorderNext(btree, val):
	
	node = getNodeObj(btree,val)
	if btree is None or node.parent is None or node is None:
		return None
	if node.parent.leftChild == node:
		return getMin(node.parent.rightChild):
	elif node.parent.rightChild == node:
		return node.parent.data