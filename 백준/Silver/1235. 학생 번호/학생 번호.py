n = int(input())
arr = []
for _ in range(n):
    l = (input())
    arr.append(l)

m = len(arr[0])
line = []
for j in range(m, 0, -1):
    for i in range(n):
        a = arr[i][j-1:m]
        if a in line:
            line.clear()
            break
        line.append(a)
    if len(line) == n:
        print(len(line[0]))
        break