count = 0
def heapify(a,n,i):
    global count
    L = i
    l = 2*i+1
    r = 2*i+2
    count +=1
    if l<n and a[l]>a[L]:
        L = l
    if r<n and a[r]>a[L]:
        L = r
    if L != i:
        a[L], a[i] = a[i], a[L]
        heapify(a,n,L)

def heapSort(a):
    n = len(a)
    for i in range(n,-1,-1):
        heapify(a,n,i)
    for i in range(n-1,0,-1):
        a[0], a[i] = a[i], a[0]
        heapify(a,i,0)

l = [7,3,9,6,2,8,9,1,4,8,6,3,9,0,4,6,6,2,9,5,7]
heapSort(l)
print(l)
print(count)