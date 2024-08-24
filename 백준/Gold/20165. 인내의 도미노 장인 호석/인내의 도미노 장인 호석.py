import sys
input = sys.stdin.readline


n,m,r = map(int, input().split())
arr=[list(map(int, input().split()))for _ in range(n)]
visited = [[True]*m for _ in range(n)]
dir = {'E':(0,1),'W':(0,-1),'S':(1,0),'N':(-1,0)}
answer = 0
def domino(x,y,d,num):
    global cnt

    if visited[x][y]:
        visited[x][y] = False
        cnt+=1

    for dis in range(num-1):
        x += dir[d][0]
        y += dir[d][1]

        if not (0<=x<n and 0<=y<m):
            continue
        if visited[x][y]:
            domino(x,y,d,arr[x][y])


for _ in range(r):
    X,Y,D = map(str, input().split())
    X = int(X)-1
    Y = int(Y)-1
    xx,yy = map(int, input().split())
    xx-=1
    yy-=1
    cnt = 0
    if visited[X][Y]:
        domino(X,Y,D,arr[X][Y])

    visited[xx][yy]=True
    answer+=cnt

print(answer)
for i in range(n):
    for j in range(m):
        if visited[i][j]:
            visited[i][j] = "S"
        else:
            visited[i][j] ="F"
    print(*visited[i])