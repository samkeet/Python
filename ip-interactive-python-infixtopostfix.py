from stack import stack

def infixToPostfix(string):
	"""
	simple infix to postfix converter
	"""

	final_string = ""
	operators = ['+','-','*','/','%','//','^']
	s = stack()
	
	for char in string:
		if char == "(":
			s.push(char)
		elif char in operators:
			s.push(char)
		elif char == ")":
			ch = s.pop()
			while ch != "(":
				final_string = final_string + ch
				ch = s.pop()
		else:
			final_string = final_string + char
	
	while s.size != 0:
		final_string = final_string + s.pop()

	print final_string