def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for x in graph[node]:
            dfs(graph,x,visited)
    return visited

def start(graph, nodes):
    allNodes = []
    for x in graph:
        allNodes+=graph[x]
    candidate = list(set(nodes) - set(allNodes))
    return candidate[0]

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

print(dfs(graph, start(graph,['a','b','c','d','e','f','g','h']), []))