import sys

input = sys.stdin.readline
n,m = map(int, input().split())
arr = [0] + list(map(int,input().split()))

sum_list = [0]*(n+1)

for i in range(1,n+1):
    sum_list[i] = sum_list[i-1] + arr[i]

for _ in range(m):
    a,b = map(int, input().split())

    print(sum_list[b]-sum_list[a]+arr[a])