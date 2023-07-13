s = int(input())
arr = [0] + list(map(int,input().split()))
st = int(input())

def change(x):
    global arr
    arr[x] = abs(arr[x]-1)
for _ in range(st):
    sex, c = map(int,input().split())
    j = 1
    if sex == 1:
        while c*j <= s:
            change(c*j)
            j+=1
    else:
        change(c)
        while 1<= c-j and c+j <=s and arr[c-j] == arr[c+j]:
            change(c-j)
            change(c+j)
            j+=1


for i in range(1, s+1):
    print(arr[i], end=" ")
    if not i % 20:
        print()