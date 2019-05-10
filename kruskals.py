def kruskals(c,n):
    ne = 1
    p = [i for i in range(n)]
    w = 0
    while ne<n:
        m = 999
        for i in range(n):
            for j in range(i+1,n):
                if c[i][j]<m:
                    m = c[i][j]
                    a = i
                    b = j
        if m==999:
            break
        u = p[a]
        v = p[b]
        if u!=v:
            print(a,"-",b," Weight=",m)
            w+=m
            p[a] = p[b]
            ne+=1
        c[a][b] = c[b][a] = 999
    if ne == n:
        print("Weight : ",w)
    else:
        print("Not connected")

n = 4
c = []
for i in range(n):
    d = []
    for j in range(n):
        x = int(input())
        if x == 0 and i != j:
            x = 999
        d.append(x)
    c.append(d)
kruskals(c,n)