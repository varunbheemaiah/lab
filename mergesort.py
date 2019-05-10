def splitArray(a):
    if len(a)>1:
        mid = len(a)//2
        b = a[:mid]
        c = a[mid:]
        splitArray(b)
        splitArray(c)
        merge(b,c,a)

def merge(b, c, a):
    i = 0
    j = 0
    k = 0
    while i<len(b) and j<len(c):
        if b[i]<=c[j]:
            a[k] = b[i]
            i+=1
        else:
            a[k] = c[j]
            j+=1
        k+=1
    while i < len(b):
        a[k] = b[i]
        i+=1
        k+=1
    while j < len(c):
        a[k] = c[j]
        j+=1
        k+=1

l = [7,3,9,6,2,8,9,1,4,8,6,3,9,0,4,6,6,2,9,5,7]
splitArray(l)
print(l)