from binarytree import BinaryTree
from stack import stack

def parseTree(exp):

	operators = ['+','-','*','/','%']
	t = BinaryTree('')
	s = stack()
	s.push(t)
	current = t

	for char in exp:
		if char == '(':
			current.setLeft('')
			s.push(current)
			current = current.getLeft()
		elif char not in operators and char != ')':
			current.setRoot(char)
			current = s.pop()
		elif char in operators:
			current.setRoot(char)
			s.push(current)
			current.setRight('')
			current = current.getRight()
		elif char == ')':
			s.pop()	
		else: raise ValueError