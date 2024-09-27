import sys
input = sys.stdin.readline
from collections import deque

N,M,K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
val = [[5]*N for _ in range(N)]
arr = [[deque() for _ in range(N)] for _ in range(N)]
dead = [[list() for _ in range(N)] for _ in range(N)]

for _ in range(M):
    a,b,c = map(int, input().split())
    arr[a-1][b-1].append(c)



dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
def spring_summer():
    global arr, A

    for i in range(N):
        for j in range(N):
            len_ = len(arr[i][j])
            for k in range(len_):
                if arr[i][j][k] > val[i][j]:
                    for _ in range(k,len_):
                        dead[i][j].append(arr[i][j].pop())
                    break
                else:
                    val[i][j] -= arr[i][j][k]
                    arr[i][j][k] += 1


    for i in range(N):
        for j in range(N):
            while dead[i][j]:
                val[i][j] += dead[i][j].pop() //2


def fall_winter():
    global arr, A

    for i in range(N):
        for j in range(N):
            len_ = len(arr[i][j])
            for k in range(len_):
                if arr[i][j][k] %5==0:
                    for t in range(8):
                        nx = dx[t] + i
                        ny = dy[t] + j
                        if 0<=nx<N and 0<=ny<N:
                            arr[nx][ny].appendleft(1)

            val[i][j] += A[i][j]

answer = 0
for _ in range(K):
    spring_summer()
    fall_winter()

for i in range(N):
    for j in range(N):
        answer += len(arr[i][j])

print(answer)