def bfs(graph, start, visited):
    q = [start]
    while q:
        v = q.pop(0)
        if not v in visited:
            visited+=[v]
            q+=graph[v]
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

print(bfs(graph, 'f', []))