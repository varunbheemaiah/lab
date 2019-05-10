def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for x in graph[node]:
            dfs(graph,x,visited)
    return visited

graph = {
    'a': ['b'],
    'b': ['c','d'],
    'c': ['e'],
    'd': ['e'],
    'e': [],
    'f': ['g','h'],
    'g': [],
    'h': []
}

print(dfs(graph, 'a', []))