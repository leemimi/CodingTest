k = int(input())

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(str, input().split())))
time = 210
for i in range(n):
    t, a = arr[i]
    t = int(t)
    time -= t

    if(time < 0):
        break
    if a == 'T':
        k+= 1
        if(k >= 9):
            k = 1

print(k)