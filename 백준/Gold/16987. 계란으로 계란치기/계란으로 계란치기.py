import sys
input = sys.stdin.readline

n = int(input())
arr = []

def check(arr):
    cnt = 0
    for a in arr:
        if a[0]<=0:
            cnt+=1
    return cnt

def bt(v,arr):
    global res
    if v == n:
        res = max(res, check(arr))
        return

    if arr[v][0] <= 0:
        bt(v+1,arr)

    else:
        flag = True
        for i in range(n):
            if v != i and arr[i][0] >0:
                flag = False
                arr[v][0]-=arr[i][1]
                arr[i][0] -= arr[v][1]
                bt(v+1,arr)
                arr[v][0] += arr[i][1]
                arr[i][0] += arr[v][1]
        if flag:
            bt(n,arr)


for _ in range(n):
    a,b = map(int, input().split())
    arr.append([a,b])
res = 0
bt(0,arr)
print(res)