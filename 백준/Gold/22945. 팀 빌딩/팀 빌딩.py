import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

lt=0
rt=n-1

def cal(a,b,c):
    return c*min(a,b)

res = 0
while lt + 1< rt:

    t = cal(arr[lt],arr[rt],abs(rt-lt-1))
    res = max(t, res)
    if arr[lt] < arr[rt]:
        lt+=1
    else:
        rt-=1

print(res)