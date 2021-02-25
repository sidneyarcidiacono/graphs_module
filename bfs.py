"""Implement breadth-first search using the given graph representation."""

graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F'],
  'D': [],
  'E': ['F'],
  'F': []
}

visited = []


def bfs(visited, graph, node):
    """
    Visit each node in graph.

    graph: Type=adjacency list.
    node: Type=Any primitive
    return: Type=None, just visit & print each node.
    """
    queue = []
    # append node to queue
    queue.append(node)
    # append node to visited
    visited.append(node)

    while queue:
        # n is queue.pop()
        n = queue.pop(0)
        # visit graph["n"]
        print(n)
        # print each item in values list
        for i in graph[n]:
            if i not in visited:
                # append each item in values list to queue only
                # IF not in visited
                queue.append(i)
                visited.append(i)
    return


print(bfs(visited, graph, "A"))
