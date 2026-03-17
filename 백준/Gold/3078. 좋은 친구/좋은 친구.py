import sys
input = sys.stdin.readline
from  collections import defaultdict
n,k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(len(input().strip()))


dit = defaultdict(int)
cnt = 0
for i in range(n):
    if i > k:
        dit[arr[i-k-1]] -=1
    cnt += dit[arr[i]]
    dit[arr[i]] +=1

print(cnt)