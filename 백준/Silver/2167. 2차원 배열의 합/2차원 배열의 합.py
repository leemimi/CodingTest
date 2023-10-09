n,m = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(n)]
B = [[0]*(m+1) for _ in range(n+1)]


for i in range(1,n+1):
    for j in range(1, m+1):
        B[i][j] = B[i-1][j] + B[i][j-1] - B[i-1][j-1] + arr[i-1][j-1]

t = int(input())
for _ in range(t):
    x1,y1,x2,y2 = map(int, input().split())

    print(B[x2][y2] - B[x2][y1-1] - B[x1-1][y2] + B[x1-1][y1-1])