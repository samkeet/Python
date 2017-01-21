from binarytree import BinaryTree
from linkedlist import Node, LinkedList

def listofdepths(btree):

	result = []
	list_nodes = LinkedList()
	if btree is not None:
		list_nodes.insertStart(btree)
	else:
		return None

	while list_nodes.size > 0:
		result.append(list_nodes)
		parents = list_nodes
		list_nodes = LinkedList()
		print list_nodes
		# while parents:
		# 	if parents.data.leftChild:
		# 		list_nodes.insertStart(parents.data.leftChild)
		# 	elif parents.data.rightChild:
		# 		list_nodes.insertStart(parents.data.rightChild)
		# 	parents = parents.ext

	return result

btree = BinaryTree(6)
btree.setLeft(4)
btree.setRight(7)
btree.leftChild.setLeft(2)
btree.leftChild.setRight(5)
btree.rightChild.setLeft(6)
btree.rightChild.setRight(9)
		
listofdepths(btree)