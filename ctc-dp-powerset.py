master_list = []

def main(set):
	if len(set) == 0:
		return []
	else:
		return powerset(set) + [[]]

def powerset(set,master_list):
	if set in master_list:
		return master_list
	elif len(set) == 1:
		if set not in master_list:
			master_list += set
	else:
		for i in range(len(set)):
			temp = set.remove(set[i])
			if temp not in master_list:
				master_list += powerset(temp)
	return master_list


# for checking if a list is in master time = len(master)*len(list)		