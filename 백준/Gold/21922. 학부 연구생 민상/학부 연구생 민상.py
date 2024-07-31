from collections import deque
import sys

# 다시 돌아오는 경우에 바람을 그 자리에서 사라진다고 생각하면 
# 굳이 방문 배열을 3차원으로 관리 하지 않아도 된다.
# 어차피 내가 이미 방문했던 지점을 다시 탐색하게 되기 때문이다.

si = sys.stdin.readline

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

n, m = map(int, si().split())
visited = [[0] * m for _ in range(n)]

# 에어컨의 위치를 담는 큐 
q = deque()
graph = []

for i in range(n):
    line = list(map(int, si().split()))
    for j in range(m):
        # 에어컨 위치 미리 큐에 넣어 놓기
        if line[j] == 9:
            q.append((i, j))
            visited[i][j] = 1
    graph.append(line)


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


# 바람이 이동하는 루트가 겹치지 않도록, 겹치는 경우에는 루프 탈출
def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            dx, dy = dxs[i], dys[i]
            nx, ny = x + dx, y + dy

            while in_range(nx, ny):
                # 방문 체크
                visited[nx][ny] = 1
                # 에어컨 위치로 이동한 경우
                if graph[nx][ny] == 9:
                    break
                # 3 물건, 방향 전환
                if graph[nx][ny] == 3:
                    dx, dy = -dy, -dx
                 # 4 물건, 방향 전환
                elif graph[nx][ny] == 4:
                    dx, dy = dy, dx
                # 1, 2 물건을 정면으로 마주치는 바람 이동 종료
                elif (graph[nx][ny] == 1 and dx == 0) or (graph[nx][ny] == 2 and dy == 0):
                    break

                # 다음 위치를 갱신
                nx += dx
                ny += dy


bfs()

answer = 0
# 방문한 점들의 개수를 카운트 
for i in range(n):
    for j in range(m):
        if visited[i][j] == 1:
            answer += 1

print(answer)