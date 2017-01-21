row_max = 10
col_max = 6
visited = []

def main(maze):

	if maze is None:
		return False
	return wayDown(0,0)

def wayDown(row, col):
	global visited

	if row == row_max or col == col_max or maze[row][col] == 'N':
		visited[row][col] = True
		return False
	elif visited[row][col]:
		return False
	elif maze[row][col] == 'Final' or wayDown(row-1, col+1) or wayDown(row,col+1)
		visited[row][col] = True
		return True