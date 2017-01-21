from graphgeneral import Graph, Vertex

def dfs(g,start):

	unvisited = []
	visited = []
	unvisited.append(start)

	while unvisited:
		print "Going to: " + str(unvisited)
		u = unvisited[0]
		unvisited.remove(u)
		neighbours = g[u]
		print str(u) + " is connected to: " + str(neighbours)
		for v in  neighbours:
			if v not in visited:
				unvisited.append(v)
		visited.append(u)
	print visited

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
#print g.nodes
#for v in g.getVertices():
#	print g[v]

bfs(g, 0)