class Graph(object):

	def __init__(self, adj_list = {}):
		self.adj_list = adj_list
		self.nodes = 0

	def addVertex(self, key):
		node = Vertex(key)
		self.adj_list[key] = node
		self.nodes += 1		

	def addEdge(self, start, end, weight):
		if start not in self.adj_list:
			self.addVertex(start)
		if end not in self.adj_list:
			self.addVertex(end)
		self.adj_list[start].addNeighbour(end,weight)

	def getEdges(self,start):
		if start not in self.adj_list:
			return None
		else:
			return self.adj_list[start].getNeighbours()

	def removeVertex(self,node):
		del self.adj_list[start]
		self.nodes -= 1

	def removeEdge(self, start, end):
		if start not in self.adj_list or end not in self.adj_list:
			raise ValueError('Invalid Edge')
		else:
			self.adj_list[start].removeNode(end)

	def getVertices(self):
		return [x for x in self.adj_list]

	def __getitem__(self, node):
		return self.getEdges(node)

	def __contains__(self, node):
		if node in self.adj_list:
			return True
		else:
			return False

	def __delitem__(self, node):
		self.removeVertex(node)

	def __iter__(self):
		return iter(self.adj_list.values())

class Vertex(object):

	def __init__(self, key = None):
		self.key = key
		self.neighbours = {}

	def addNeighbour(self, end, weight):
		self.neighbours[end] = weight

	def getNeighbours(self):
		return [x for x in self.neighbours]

	def removeNeighbour(self, node):
		del self.neighbours[node]

	def getId(self):
		return self.key

	def __str__(self):
		return str(self.key) + " Connected to " + str([x for x in self.neighbours])