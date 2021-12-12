def readfile(filename):
    graph = {}

    with open(filename) as f:
        for line in f.readlines():
            vert1, vert2 = line.strip().split('-')
            if vert1 not in graph:
                graph[vert1] = []
            if vert2 not in graph:
                graph[vert2] = []
            graph[vert1].append(vert2)
            graph[vert2].append(vert1)

    return graph


def visit(graph, vert, already_visited):
    if vert == 'end':
        return 1

    neighbours = filter(lambda v: v not in already_visited, graph[vert])
    new_already_visited = already_visited.copy()

    if vert.islower():
        new_already_visited.add(vert)

    s = 0
    for neigh in neighbours:
        s += visit(graph, neigh, new_already_visited)

    return s


graph = readfile('input1')

s = visit(graph, 'start', set())
print(s)
