def anagramsGroup(strs):
	list_hashmaps = []
	list_anagrams = []
	for string in strs:
		h = {}
		for char in string:
			if char not in h:
				h[char] = string.count(char)
		list_hashmaps.append(h)
	
	print list_hashmaps
	visited = []
	for i in range(0,len(list_hashmaps)):
		if strs[i] not in visited:
			l = []
			l.append(strs[i])
			for j in range (i+1,len(list_hashmaps)):
				if list_hashmaps[i] == list_hashmaps[j]:
					l.append(strs[j])
					visited.append(strs[j])
			list_anagrams.append(l)
	print list_anagrams
anagramsGroup(["", "b"])


