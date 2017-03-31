class Graphs(object):
    def __init__(self):
        self.adj_list = None
        self.adj_mat = None

    def bfs(self):
        if self.adj_list is None:
            return -1
        
