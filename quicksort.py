def partition(a,low,high):
    pivot = a[low]
    i = low
    j = high+1
    while True:
        while True:
            i += 1
            if a[i]>=pivot: break
        while True:
            j -= 1
            if a[j]<=pivot: break
        a[i], a[j] = a[j], a[i]
        if i>=j: break
    a[i], a[j] = a[j], a[i]
    a[low], a[j] = a[j], a[low]
    return j

def quick(a, low, high):
    if low<high:
        s = partition(a,low,high)
        quick(a,low,s-1)
        quick(a,s+1,high)

l = [7,3,9,6,2,8,9,1,4,8,6,3,9,0,4,6,6,2,9,5,7]
quick(l,0,len(l)-1)
print(l)