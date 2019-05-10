numNodes = int(input("Enter the number of nodes : "))
weightedMatrix = [[0 for x in range(numNodes)] for y in range(numNodes)]
print("Enter the weighted matix : ")
for i in range(numNodes):
	for j in range(numNodes):
		weightedMatrix[i][j]=int(input())

print("The entered adjacency matrix is : ")
for i in range(numNodes):
	for j in range(numNodes):
		print(weightedMatrix[i][j],end=" ")
	print("")

for k in range(numNodes):
	for i in range(numNodes):
		for j in range(numNodes):
			weightedMatrix[i][j]=min(weightedMatrix[i][j],(weightedMatrix[i][k]+weightedMatrix[k][j]))

print("")

for i in range(numNodes):
	for j in range(numNodes):
		print(weightedMatrix[i][j],end=" ")
print("")