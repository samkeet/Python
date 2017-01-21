def anagram(strs):

	h = {}
	for string in strs:
		temp = ''.join(sorted(string))
		if temp in h:
			buff = h.get(temp)
			buff.append(string)
		else:
			h[temp] = [string]

	print h.values()

anagram(["eat", "tea", "tan", "ate", "nat", "bat"])