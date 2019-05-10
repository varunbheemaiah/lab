def bubsort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1], a[j]

l = [7,3,9,6,2,8,9,1,4,8,6,3,9,0,4,6,6,2,9,5,7]
bubsort(l)
print(l)