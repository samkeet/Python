from stack import stack

def twoLitres(jug_one, jug_two):

	while jug_one != 2:

		if jug_one < 4:
			jug_one =4
		
		print jug_one, jug_two

		diff = jug_one - jug_two
		if diff > 3:
			diff = 3 
		jug_one = jug_one-diff
		jug_two = jug_two+diff
		if jug_two > 3:
			jug_two = 3

		print jug_one, jug_two

		if jug_two > 0:
			jug_two = 0

		print jug_one, jug_two

		diff = jug_one - jug_two
		if diff > 3:
			diff = 3
		jug_one = jug_one-diff
		jug_two = jug_two+diff
		if jug_two > 3:
			jug_two = 3
		print jug_one, jug_two

print twoLitres(0,0)