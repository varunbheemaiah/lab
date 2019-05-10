n = int(input())
board = [[0 for i in range(n)] for j in range(n)]

def issafe(row,col):
    for i in range(col):
        if board[row][i]:
            return 0
    for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
        if board[i][j]:
            return 0
    for i,j in zip(range(row,n), range(col,-1,-1)):
        if board[i][j]:
            return 0
    return 1

def solve(col):
    if col>=n:
        return 1
    for i in range(n):
        if(issafe(i,col)):
            board[i][col] = 1
            if solve(col+1):
                return 1
            board[i][col] = 0
    return 0

def solveNQ():
    if solve(0) == 0:
        print("No solution")
    for x in board:
        print(x)

solveNQ()