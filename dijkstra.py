def mindist(dist, sptset, n):
    min = 99999
    min_index = 0
    for v in range(n):
        if sptset[v] == False and dist[v]<=min:
            min = dist[v]
            min_index = v
    return min_index

def dijkstra(graph, src, n):
    dist = [99999 for i in range(n)]
    sptset = [False for i in range(n)]
    dist[src] = 0
    for i in range(n-1):
        u = mindist(dist, sptset, n)
        sptset[u] = True
        for v in range(n):
            if not sptset[v] and graph[u][v] and dist[u] != 99999 and dist[u]+graph[u][v]<dist[v]:
                dist[v] = dist[u]+graph[u][v]
    for i in range(n):
        print(i," : ",dist[i])

a = [
    [0,1,1,0],
    [0,0,0,2],
    [0,0,0,5],
    [0,0,0,0]
]

dijkstra(a, 0, 4)