n= int(input())
arr = input()

r = arr.count('R')
b = n -r
cnt = 0
ans = min(r,b)

for i in range(n):
    if arr[i] != arr[0] :
        break
    cnt +=1
if arr[0] == 'R' :
    ans = min(ans, r -cnt)
else:
    ans = min(ans, b -cnt)

cnt = 0
for i in range(n-1,-1,-1):
    if arr[i] != arr[n-1]:
        break
    cnt +=1
if arr[n-1] == 'R':
    ans = min(ans, r - cnt)
else:
    ans = min(ans, b-cnt)

print(ans)
