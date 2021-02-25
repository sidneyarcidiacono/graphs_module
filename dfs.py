"""Implement depth-first search using the given graph representation."""

graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F'],
  'D': [],
  'E': ['F'],
  'F': []
}


def recursive_dfs(graph, node, path=[]):
    """Recursive depth-first search."""
    if node not in path:
        path.append(node)

        if node not in graph:
            # leaf node, backtrack
            return path

        for neighbour in graph[node]:

            path = recursive_dfs(graph, neighbour, path)

    return path


print(recursive_dfs(graph, "A"))
