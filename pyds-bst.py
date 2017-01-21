class BST(object):

	def __init__(self, root = None):
		self.root = root
		self.size = 0

	def __iter__(self):
		return self.root.__iter__()

	def __len__(self):
		return self.size

	def length(self):
		return self.size

	def get(self, key):

		if self.root:
			result = _get(key, self.root)
			if result:
				return result.payload
			else:
				return None
		else:
			return None

	def _get(key, curentNode):

		if not curentNode:
			return None
		elif curentNode.key == key:
			return curentNode
		elif currentNode.key >= key:
			return _get(key, curentNode.leftChild)
		else:
			return _get(key, curentNode.rightChild)

	def __getitem__(self, key):
		return self.get(key)


	def put(self,key,payload):
		if self.root:
			self.root._put(key,payload,self.root)
		else:
			self.root = BSTNode(key,payload)
		self.size += 1

	def _put(self,key,payload,currentNode):
		if key < currentNode.key:
			if currentNode.hasLeft():
				_put(key,payload,currentNode.leftChild)
			else:
				curentNode.leftChild = BSTNode(key,payload)
		else:
			if currentNode.hasRight():
				_put(key,payload,currentNode.rightChild)
			else:
				currentNode.rightChild = BSTNode(key,payload)
		self.size += 1

	def __setitem__(self,key,data):
		self.put(key,data)

	def __contains__(self,key):
		if self.get(key):
			return True
		else:
			return False

	def delete(self, key):
		if self.size > 1:
			nodeToRemove = self.__get(key)
			if nodeToRemove:
				self.remove(nodeToRemove)
				self.size = self.size - 1
			else:
				raise KeyError('Key does not exists')
		elif self.size == 1 and self.root.key == key:
			self.root = None
			self.size = self.size - 1
		else:
			raise KeyError('Key not found')

	def __delitem__(self,key):
		return self.delete(key)

	def spliceOut(self):
		if self.isLeaf():
			if self.isLeftChild():
				self.parent.leftChild = None
			else:
				self.parent.rightChild = None
		elif self.hasAnyChildren():
			if self.hasLeft():
				if self.isLeftChild():
					self.parent.leftChild = self.leftChild
				else:
					self.parent.leftChild = self.rightChild
				self.leftChild.parent = self.parent
			else:
				if self.isLeftChild():
					self.parent.leftChild = self.rightChild
				else:
					self.parent.rightChild = self.rightChild
				self.rightChild.parent = self.parent


	def findMin(self):

		curentNode = self
		while curentNode.hasLeft():
			curentNode = curentNode.leftChild
		return currentNode

	def findSuccessor():

		succ = None
		if self.hasRight():
			succ = self.rightChild.findMin()
		else:
			if self.parent:
				if self.isLeftChild():
					succ = self.parent
				else:
					self.parent.rightChild = None
					succ = self.parent.findSuccessor()
					self.parent.rightChild = self
		return succ

	def remove(self,currentNode):

		if currentNode.isLeaf():
			if currentNode.isLeftChild():
				self.parent.leftChild = None
			else:
				self.parent.rightChild = None
		elif currentNode.hasBothChildren():
			succ = currentNode.findSuccessor()
			succ.spliceOut()
			currentNode.key = succ.key
			currentNode.payload = succ.payload
		# node has only one child
		else:
			if currentNode.isLeftChild():
				if currentNode.hasLeft():
					currentNode.parent.leftChild = currentNode.leftChild
					currentNode.leftChild.parent = currentNode.parent
				elif currentNode.hasRight():
					curentNode.parent.leftChild = currentNode.rightChild
					currentNode.rightChild.parent = currentNode.parent
				else:
					currentNode.replaceNodeData(currentNode.leftChild.key,
                                    currentNode.leftChild.payload,
                                    currentNode.leftChild.leftChild,
                                    currentNode.leftChild.rightChild)
			else:
				if currentNode.hasRight():
					currentNode.parent.rightChild = currentNode.rightChild
					currentNode.rightChild = currentNode.parent
				elif currentNode.hasLeft():
					currentNode.parent.rightChild = currentNode.leftChild
					currentNode.leftChild = currentNode.parent
				else:
					currentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.payload,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)

class BSTNode(object):

	def __init__(self, key, val, leftChild = None, rightChild = None, parent = None):
		self.key = key
		self.payload = val
		self.leftChild = leftChild
		self.rightChild = rightChild
		self.parent = parent

	def hasLeft(self):
		return self.leftChild

	def hasRight(self):
		return self.rightChild

	def hasParent(self):
		return not self.parent

	def isLeaf(self):
		return not (self.leftChild or self.rightChild)

	def hasAnyChildren(self):
		return self.leftChild or self. rightChild

	def hasBothChildren(self):
		return self.leftChild and self.rightChild

	def isLeftChild(self):
		return self.parent.leftChild == self and self.parent

	def isRightChld(self):
		return self.parent.rightChild == self and self.parent