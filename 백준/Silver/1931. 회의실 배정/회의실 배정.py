N = int(input())
arr=[]
for _ in range(N):
    a,b = map(int, input().split())
    arr.append([a,b])

arr.sort(key=lambda x:x[0])
arr.sort(key=lambda x:x[1])
cnt=0
last=0
for time in arr:
    start, end = time[0],time[1]

    if start >= last:
        cnt+=1
        last = end


print(cnt)