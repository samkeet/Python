from bst import BST, BSTNode

def createMinimalBST(list_of_nodes):

	if len(list_of_nodes) == 1:
		return BSTNode(list_of_nodes[0])
	else:
		len_list = len(list_of_nodes)
		mid = list_of_nodes[len_list//2]
		root_node = BSTNode(mid)
		root_node.leftChild = createMinimalBST(list_of_nodes[:len_list])
		root_node.rightChild = createMinimalBST(list_of_nodes[mid+1:])
		return root_node


createMinimalBST([1,2,3,4,5,6,7,8,9])