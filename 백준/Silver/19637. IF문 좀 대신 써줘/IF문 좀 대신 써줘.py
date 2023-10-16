import sys
input = sys.stdin.readline
n,m = map(int, input().split())
rank = []
def bs(rank,cnt):
    st, end = 0, len(rank)-1
    res = 0
    while st<=end:
        mid = (st+end)//2
        if int(rank[mid][1])>=cnt:
            end = mid -1
            res = mid
        else:
            st = mid +1
    return res


for _ in range(n):
    name, hp = map(str, input().split())
    rank.append([name,hp])

for _ in range(m):
    n = int(input())
    print(rank[bs(rank,n)][0])