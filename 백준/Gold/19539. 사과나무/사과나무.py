n = int(input())
arr = list(map(int, input().split()))

cnt = 0
if sum(arr)%3==0:
    for a in arr:
        cnt +=  a//2
    if cnt >= (sum(arr)//3):
        print("YES")
    else:
        print("NO")
else:
    print("NO")