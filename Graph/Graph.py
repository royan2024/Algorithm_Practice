class Graph:
    def __init__(self, vert_size):
        self.vert_size = vert_size
        self.edges = []
        for i in range(self.vert_size):
            l = []
            for j in range(self.vert_size):
                l.append(0)
            self.edges.append(l)

    def __str__(self):
        s = ""
        for i in range(self.vert_size):
            s += str(self.edges[i])
            s += "\n"
        return s

    def get_verts(self):
        return list(range(self.vert_size))

    def add_edge(self, start, end, value):
        if start > self.vert_size or end > self.vert_size:
            raise Exception("(%d, %d) is out of range: %d" % (start, end, self.vert_size))

        self.edges[start - 1][end - 1] = value
        self.edges[end - 1][start - 1] = value


if __name__ == "__main__":
    graph = Graph(6)
    print(graph)
    graph.add_edge(1, 2, 7)
    graph.add_edge(1, 3, 9)
    graph.add_edge(1, 6, 14)
    graph.add_edge(2, 3, 10)
    graph.add_edge(2, 4, 15)
    graph.add_edge(3, 4, 11)
    graph.add_edge(3, 6, 2)
    graph.add_edge(6, 5, 9)
    graph.add_edge(4, 5, 6)
    print(graph)
