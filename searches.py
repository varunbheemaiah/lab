import random
import xlsxwriter

workbook = xlsxwriter.Workbook('arrays.xlsx')
worksheet = workbook.add_worksheet()

def linear(a, ele):
    count = 0
    for i in range(len(a)):
        count = count + 1
        if a[i] == ele:
            return (count)

def binary(a, ele):
    count = 0
    low = 0
    high = len(a)-1
    while low <= high:
        mid = (low+high)//2
        count+=1
        if a[mid] == ele:
            return (count)
        elif ele<a[mid]:
            high = mid-1
        else:
            low = mid+1
    return (count)

def inter(a, ele):
    count = 0
    low = 0
    high = len(a)-1
    while low <= high:
        if low == high:
            if a[low] == ele:
                return low
            return -1
        mid = low + int(((float(high-low)/(a[high]-a[low]))*(ele-a[low])))
        count+=1
        if a[mid] == ele:
            return (count)
        elif ele<a[mid]:
            high = mid-1
        else:
            low = mid+1
    return (count)

aCount = []
linCount = []
binCount = []
intCount = []
_ = 50
for _ in range(50,100,5):
    aCount.append(_)
    a = [random.randint(0,100) for i in range(_)]
    ele = random.choice(a)
    a.sort()
    L = linear(a,ele)
    B = binary(a,ele)
    I = inter(a,ele)
    linCount.append(L)
    binCount.append(B)
    intCount.append(I)
allData = [aCount,linCount,binCount,intCount]
row = 0
for col, data in enumerate(allData):
    worksheet.write_column(row, col, data)
workbook.close()
    