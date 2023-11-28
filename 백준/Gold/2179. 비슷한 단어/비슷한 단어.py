n = int(input())
a = [input() for _ in range(n)]
arr = sorted(list(enumerate(a)), key= lambda x:x[1])

def check(a,b):
    cnt = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            cnt+=1
        else:
            break
    return cnt

length = [0]*(n+1)
maxlength = 0


for i in range(n-1):
    tmp = check(arr[i][1],arr[i+1][1])
    maxlength = max(tmp, maxlength)

    length[arr[i][0]] = max(length[arr[i][0]],tmp)
    length[arr[i+1][0]] = max(length[arr[i+1][0]], tmp)

first = 0
for i in range(n):
    if first == 0:
        if length[i] == max(length):
            first = a[i]
            print(first)
            pre = a[i][:maxlength]
    else:
        if length[i] == max(length) and a[i][:maxlength] == pre:
            print(a[i])
            break