import sys
input = sys.stdin.readline


n = int(input())
arr = []
for _ in range(n):
    a = input().rstrip()
    arr.append(a)

dict = {}
for i in range(n):
    if arr[i] not in dict:
        dict[arr[i]] = 1
    else:
        dict[arr[i]] +=1

sv = sorted(dict.items(), key=lambda x:(-x[1],x[0]), reverse = False)
print(sv[0][0])