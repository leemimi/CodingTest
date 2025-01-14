import sys
from collections import deque, Counter

r, c = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]
work = list(map(int, input().rstrip()))

dx = [1, 1, 1, 0, 0, 0, -1, -1, -1]
dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

x, y = 0, 0
q = deque()

# 초기 설정
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'I':
            x, y = i, j
        if arr[i][j] == 'R':
            q.append((i, j))


# 미친 아두이노 이동
def go():
    global cnt, q
    new = []
    while q:
        rx, ry = q.popleft()

        # 최적 방향 계산
        min_dist = float('inf')
        nx, ny = rx, ry
        for i in range(9):
            tx = rx + dx[i]
            ty = ry + dy[i]
            if 0 <= tx < r and 0 <= ty < c:
                dist = abs(x - tx) + abs(y - ty)
                if dist < min_dist:
                    min_dist = dist
                    nx, ny = tx, ty

        # 이동 후 위치 처리
        if nx == x and ny == y:
            return False
        new.append((nx, ny))
        arr[rx][ry] = '.'

    # 충돌 처리
    map = Counter(new)
    for pos in new:
        kx, ky = pos
        if map[pos] == 1:  # 충돌이 없는 경우
            arr[kx][ky] = 'R'
            q.append(pos)
        else:  # 충돌이 있는 경우
            arr[kx][ky] = '.'  # 충돌한 위치는 빈칸 처리

    return True


# 게임 시작
cnt = 0
flag = True
for i in range(len(work)):
    w = work[i]
    nx = dx[w - 1] + x
    ny = dy[w - 1] + y

    if 0 <= nx < r and 0 <= ny < c:
        if arr[nx][ny] == 'R':  # 종수와 미친 아두이노가 충돌
            flag = False
            cnt += 1
            break
        arr[x][y] = '.'  # 기존 위치 빈칸 처리
        arr[nx][ny] = 'I'  # 종수의 새로운 위치
        x, y = nx, ny
    else:
        flag = False  # 잘못된 이동 처리
        break
    cnt+=1
    # 미친 아두이노 이동
    f = go()
    if not f:
        flag = False
        break

# 게임 결과 출력
if flag:
    for i in range(r):
        print("".join(arr[i]))
if not flag:
    print(f"kraj {cnt}")