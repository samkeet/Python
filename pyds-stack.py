class stack(object):

	def __init__(self):
		self.pointer = []
		self.size = 0

	def pop(self):
		self.size -= 1
		try:
			return self.pointer.pop()
		except Exception as e:
			raise e

	def push(self, data):
		self.pointer.append(data)	
		self.size += 1

	def peek(self):
		return self.pointer[self.size-1]

	def isEmpty(self):
		if self.size == 0:
			return True