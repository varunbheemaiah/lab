import random

def knapSack(W, wt, val, n):
    k = [[0 for i in range(W+1)] for j in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                k[i][w] = 0
            elif wt[i-1]<=w:
                k[i][w] = max(k[i-1][w] , val[i-1]+k[i-1][w-wt[i-1]])
            else:
                k[i][w] = k[i-1][w]
    return k[n][W]


W = int(input("Enter the capacity of the knapsack : "))
n = int(input("Enter the number of items : "))
wt = [random.randint(20,W+30) for i in range(n)]
val = [random.randint(20,100) for i in range(n)]

print("Weights : ",wt)
print("Values  : ",val)
print("The maximum value is : ",knapSack(W, wt, val, n))