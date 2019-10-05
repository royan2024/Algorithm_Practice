from Graph import Graph

def floyd__warshall(graph):
    verts = graph.get_verts()
    dist = graph.edges

    for k in range(len(verts)):
        for j in range(len(verts)):
            for i in range(len(verts)):
                if i != j and (dist[i][j] == 0 or dist[i][j] > dist[i][k] + dist[k][j]):
                    if dist[i][k] != 0 and dist[k][j] != 0:
                        dist[i][j] = dist[i][k] + dist[k][j]

    return dist


if __name__ == "__main__":
    graph = Graph(6)
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

    dist = floyd__warshall(graph)
    for d in dist:
        print(d)