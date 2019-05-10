def selsort(a):
    n = len(a)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if a[min]>a[j]:
                a[min], a[j] = a[j], a[min]

l = [7,3,9,6,2,8,9,1,4,8,6,3,9,0,4,6,6,2,9,5,7]
selsort(l)
print(l)