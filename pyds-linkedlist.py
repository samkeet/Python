class Node(object):

	def __init__(self, data):
		self.data = data
		self.next = None

	def setNext(self, node):
		self.next = node

	def setData(self, data):
		self.data = data

	def getNext(self):
		return self.next

	def getData(self):
		return self.data

class LinkedList(object):

	def __init__(self, head = None):
		self.head = head
		self.size = 0

	# insert in beginning	
	def insertStart(self, data):

		if self.head is None:
			self.head = Node(data)
			self.size += 1
		else:
			n = Node(data)
			n.next = self.head
			self.head = n
			self.size += 1

	def insertEnd(self, data):
		if self.head is None:
			self.head = Node(data)
			self.size += 1
		else:
			n = Node(data)
			current = self.head
			while current:
				current = current.next
			current.next = n
			self.size += 1

	def search(self, data):
		current = self.head
		if self.head.data == data:
			return head
		while current.next and not found:
			if current.next.data == data:
				return current.next
			else:
				current = current.next

	def remove(self, data):
		prev = search(data)
		prev.next = prev.next.next