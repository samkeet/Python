from graphgeneral import Graph,Vertex
#using BFS

def findPath(g,start,end):
	
	unvisited = []
	visited = []
	unvisited.append(start)

	while unvisited:
		u = unvisited[0]
		unvisited.remove(u)
		neighbours = g[u]
		print str(u) + " -> " + str(neighbours)
		for v in  neighbours:
			if v not in visited:
				if v == end:
					print True
					return True
				unvisited.append(v)
		visited.append(u)
	print False
	return False

g = Graph()
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
g.addEdge(0,6,10)
g.addVertex(7)

#findPath(g,3,7)
findPath(g,5,2)