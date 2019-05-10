def warshall(adjMat):
    D = adjMat
    n = len(adjMat)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = D[i][j] or (D[i][k] and D[k][j])
    for x in D:
        print(x)

adjMat = [
    [0,1,1,0],
    [1,0,0,0],
    [1,0,0,0],
    [0,0,0,0]
]

warshall(adjMat)