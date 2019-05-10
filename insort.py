def insort(a):
    n = len(a)
    for i in range(1,n):
        v = a[i]
        j = i-1
        while j>=0 and a[j]>v:
            a[j+1] = a[j]
            j = j-1
        a[j+1] = v

l = [7,3,9,6,2,8,9,1,4,8,6,3,9,0,4,6,6,2,9,5,7]
insort(l)
print(l)