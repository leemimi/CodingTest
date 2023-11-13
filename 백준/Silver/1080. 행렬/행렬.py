import sys
def solve(x,y,A):
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] = 1-A[i][j]


n,m = map(int,input().split())
arrA = [list(map(int, list(input()))) for _ in range(n)]
arrB = [list(map(int, list(input()))) for _ in range(n)]

res = 0
if (n<3 or m<3) and arrA != arrB :
    res = -1
else:
    for i in range(n-2):
        for j in range(m-2):
            if arrA[i][j] != arrB[i][j]:
                res +=1
                solve(i,j,arrA)

if arrA != arrB:
    print(-1)
else:
    print(res)