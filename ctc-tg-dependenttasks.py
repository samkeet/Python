def buildOrder(tasks,dependencies):
	h = {}
	task_length = len(tasks)
	for l in dependencies:
		if l[1] not in h:
			h[l[1]] = [l[0]]
		else:
			h[l[1]].append(l[0])

	for l in dependencies:
		if l[0] in tasks:
			tasks.remove(l[0])

	result = tasks
	for char in result:
		result.extend(h[char])
		if len(result) == task_length:
			break
	return result