import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr = []
dic = {}
for _ in range(n):
    s = input().rstrip()
    if len(s) < m:
        continue
    arr.append(s)

for i in range(len(arr)):
    if arr[i] not in dic:
        dic[arr[i]] = 1
    else:
        dic[arr[i]] += 1

dic = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for k,v in dic:
    print(k)