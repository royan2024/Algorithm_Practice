from Graph import Graph
import  sys

def dijkstra(graph: Graph, start):
    vertices = graph.get_verts()
    result = {}
    for v in vertices:
        if v == start:
            result[v] = 0
        else:
            result[v] = sys.maxsize


    while len(vertices) > 0:
        min_length = sys.maxsize
        pivot = start
        for v in result:
            if result[v] < min_length and v in vertices:
                pivot = v
                min_length = result[v]

        for v in vertices:
            if graph.get_edge(pivot, v) > 0:
                if result[v] > graph.get_edge(pivot, v) + min_length:
                    result[v] = graph.get_edge(pivot, v) + min_length

        vertices.remove(pivot)
    return result


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

    print(dijkstra(graph, 1))


