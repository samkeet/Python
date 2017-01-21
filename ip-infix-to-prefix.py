from infixtopostfix import infixToPostfix 

def infixToPrefix(string):
	rev_string = ""
	strlen = len(string)
	for index in range(strlen-1,-1,-1):
		rev_string = rev_string + string[index]

	
	infixToPostfix(rev_string)

infixToPrefix('(a+B)')