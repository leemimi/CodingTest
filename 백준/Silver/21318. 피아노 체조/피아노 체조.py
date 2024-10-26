import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
val = [0]*n
val[0] = 0
for i in range(n-1):
    if arr[i] > arr[i+1]:
        val[i] = 1
pre_sum = [0]*(n+1)
for i in range(1,n+1):
    pre_sum[i] = val[i-1] + pre_sum[i-1]
Q = int(input())
for _ in range(Q):
    x,y = map(int, input().split())
    print(pre_sum[y-1]-pre_sum[x-1])