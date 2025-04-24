n, attack = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
hp = 0

lt = 1
rt = 10**18
res = 0
while lt <= rt:
    atk = attack
    mid = (lt + rt) // 2
    hp = mid
    flag  = True
    for i in range(n):
        t, a, h = arr[i]
        if t == 1:
            hit = (h+atk-1)//atk
            hp -= (hit-1) * a
            if hp <= 0:
                flag = False
                break

        elif t == 2:
            atk += a
            hp = min(hp+h, mid)

    if flag:
        res = mid
        rt = mid -1
    else:
        lt = mid + 1

print(res)