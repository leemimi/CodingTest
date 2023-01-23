from collections import deque

n,k = map(int,input().split())

won = deque(range(1,n+1))
cnt =0
arr =[]
while True:
    if len(won) == 0:
        break
    cnt +=1
    if cnt == k:
        a=won.popleft()
        arr.append(a)
        cnt =0
    else:
        cur = won.popleft()
        won.append(cur)
print("<", end='')
for i in range(len(arr)-1):
    print(arr[i],end=', ')
print(arr[-1],end='')
print(">")