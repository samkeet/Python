steps = {}
graph = []
def main(n):
	return countSteps(n)

def countSteps(n):
	global steps
	global graph
	graph.append(n)

	if n == 0:
		return 0
	elif n == 1:
		return 1
	elif n == 2:
		return 2
	elif n == 3:
		return 3 
	elif n in steps:
		return steps[n]
	else:
		steps[n] = countSteps(n-1) + countSteps(n-2) + countSteps(n-3)
		return steps[n]

print main(10)
print steps
print graph
print len(graph)