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


def visit(graph, vert, path, path_has_double):
    if vert == 'end':
        return 1
    if len(path) > 0 and vert == 'start': # accidentally came back, cut off
        return 0

    s = 0

    if vert.islower() and vert in path:
        path_has_double = True


    if path_has_double:
        neighbours = list(filter(lambda v: v.isupper() or v not in path, graph[vert]))
    else:
        neighbours = graph[vert]

    new_path = path.copy() 
    new_path.append(vert)

    for n in neighbours:
        s += visit(graph, n, new_path, path_has_double)

    return s


graph = readfile('input1')

s = visit(graph, 'start', [], False)
print(s)
