class BinaryTree(object):

	def __init__(self, data = ''):
		self.data = data
		self.leftChild = None
		self.rightChild = None

	def setRight(self, data):
		self.rightChild = BinaryTree(data)

	def setLeft(self, data):
		self.leftChild = BinaryTree(data)

	def getRight(self):
		return self.leftChild

	def getLeft(self):
		return self.rightChild

	def setRoot(self, data):
		self.data = data

	def getRoot(self):
		return self.data

def preorder(node):
	if node:
		print node.getRoot()
		preorder(node.getLeft())
		preorder(node.getRight())

def inorder(node):
	if node:
		inorder(node.getLeft())
		print node.getRoot()
		inorder(node.getRight())

# def postorder(self):
# 	if self:
# 		preorder(self.getLeft())
# 		preorder(self.getRight())
# 		print self.getRoot()

# btree = BinaryTree(6)
# btree.setLeft(4)
# btree.setRight(7)
# btree.leftChild.setLeft(2)
# btree.leftChild.setRight(5)
# btree.rightChild.setLeft(6)
# btree.rightChild.setRight(9)

#preorder(btree)
#inorder(btree)