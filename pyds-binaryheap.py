from binarytree import BinaryTree
class binaryHeap(object):

	def __init__(self, root = None):
		self.root = rooterr
		self.left_size = 0
		self.right_size = 0

	def insert(self, data):
		if self.root == None:
			root = BinaryTree(data)

		elif data >= node.getData():
			if self.right_size >= self.left_size:
				node = node.getRight()
				node.insert(data)
			else:
				node = node.getLeft()
				node.insert(data)

		elif data < self.root.getData():
			if self.root.left_size >= self.root.right_size:
				n = BinaryTree(data)
				n.leftChild = self.root.getLeft()
				n.rightChild = self.root
				self.root.leftChild = None