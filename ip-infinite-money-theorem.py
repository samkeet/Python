import random
_space = " "

def generateString(length, inputstr):
	global _space
	alphabet = "abcdefghijklmnopqrstuvwxyz "
	res = ""
	for i in range(length):
		if inputstr[i] == _space:
			res = res + alphabet[random.randrange(27)]
			#print res
		else:
			res = res + inputstr[i]
	return res

def stringScore(goal, string):
	global _space
	count = 0
	res = ""
	if goal == string:
		return [goal, 1]
	for i in range(len(goal)):
		if goal[i] == string[i]:
			res = res + goal[i]
			count += 1
		else:
			res = res + _space
		#print res

	return [res, float(count) / float(len(goal))]


def main():
	f = open("weasel-output.txt","wb")
	goalstring, newstring = "methinks it is like a weasel", " "*28
	newscore, bestscore, iterations, strlen, _million = 0,0,0,28,1000000

	while newscore < 1:
		arr = stringScore(goalstring, newstring)
		newstring = arr[0]
		newscore = arr[1]
		if newscore > bestscore: bestscore = newscore
		if iterations % _million == 0: 
			print bestscore, newstring
		iterations += 1
		newstring = generateString(strlen, newstring)
		f.write(newstring+"\n")
	f.close()
	print iterations
	print newstring
	print len(newstring)
main()