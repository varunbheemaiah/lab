def prims(c,n):
    ne = 1
    w = 0
    v = [0]
    while ne<n:
        m = 999
        for i in v:
            for j in range(n):
                if j not in v:
                    if c[i][j]<m:
                        m = c[i][j]
                        a = i
                        b = j
        if m==999:
            break
        ne += 1
        w += m
        v.append(b)
        print(a,"-",b," Weight : ",m)
    if ne == n:
        print("Weight : ",w)
    else:
        print("Disconnected")



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
prims(c,n)