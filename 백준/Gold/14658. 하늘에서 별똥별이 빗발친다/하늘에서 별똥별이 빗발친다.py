import sys
input = sys.stdin.readline

N, M, L, K = map(int, input().split())
tmp = [list(map(int, input().split())) for _ in range(K)]


min_num = 0

for i in range(len(tmp)):
    for j in range(len(tmp)):
        cnt = 0
        for cur in range(len(tmp)):
            r,c = tmp[cur]
            if tmp[i][0] <= r <= tmp[i][0]+L and tmp[j][1] <= c<= tmp[j][1]+L:
                cnt+=1

        min_num = max(cnt, min_num)

print(K-min_num)