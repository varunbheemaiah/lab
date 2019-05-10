def start(graph,nodes):
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
}
nodes = ['b','c','a','e','d']

topsort = []
for i in range(len(nodes)):
    topsort.append(start(graph,nodes))
    graph.pop(topsort[i])
    nodes.remove(topsort[i])
    print(graph)
print(topsort)