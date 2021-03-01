def BFS(graph, start, end, to_print=False):
    '''Assumes graph is a Digraph; start and end are nodes
    Returns a shortest path from start to end in graph'''
    init_path = [start]
    path_queue = [init_path]
    while len(path_queue) != 0:
        # Get and remove oldest element in path_queue
        tmp_path = path_queue.pop(0)
        if to_print:
            print('Current BFS path:', print_path(tmp_path))
        last_node = tmp_path[-1]
        if last_node == end:
            return tmp_path
        for next_node in graph.children_of(last_node):
            if next_node not in tmp_path:
                new_path = tmp_path + [next_node]
                path_queue.append(new_path)
    return None


sp = BFS(g, nodes[0], nodes[5])
print('Shortest path found by BFS:', print_path(sp))
