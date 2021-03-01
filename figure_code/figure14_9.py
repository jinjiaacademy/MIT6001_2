def print_path(path):
    '''Assumes path is a list of nodes'''
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result


def DFS(graph, start, end, path, shortest, to_print=False):
    '''Assumes graph is a Digraph; start and end are nodes;
            path and shortest are lists of nodes
    Returns a shortest path from start to end in graph'''
    path = path + [start]
    if to_print:
        print('Current DFS path:', print_path(path))
    if start == end:
        return path
    for node in graph.children_of(start):
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                new_path = DFS(graph, node, end, path, shortest, to_print)
                if new_path != None:
                    shortest = new_path
    return shortest


def shortest_path(graph, start, end, to_print=False):
    '''Assumes graph is a Digraph; start and end are nodes
    Returns a shortest path from start to end in graph'''
    return DFS(graph, start, end, [], None, to_print)


def test_SP():
    nodes = []
    for name in range(6):
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.add_node(n)
    g.add_edge(Edge(nodes[0], nodes[1]))
    g.add_edge(Edge(nodes[1], nodes[2]))
    g.add_edge(Edge(nodes[2], nodes[3]))
    g.add_edge(Edge(nodes[2], nodes[4]))
    g.add_edge(Edge(nodes[3], nodes[4]))
    g.add_edge(Edge(nodes[3], nodes[5]))
    g.add_edge(Edge(nodes[0], nodes[2]))
    g.add_edge(Edge(nodes[1], nodes[0]))
    g.add_edge(Edge(nodes[3], nodes[1]))
    g.add_edge(Edge(nodes[4], nodes[0]))
    sp = shortest_path(g, nodes[0], nodes[5], to_print=True)
    print('Shortest path found by DFS:', print_path(sp))

test_SP()
