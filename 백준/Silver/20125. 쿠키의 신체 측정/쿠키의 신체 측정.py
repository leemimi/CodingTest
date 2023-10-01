n = int(input())
arr = [list(map(str, input())) for _ in range(n)]

x = 0
y = 0
sign = False
for i in range(n):
    for j in range(n):
        if arr[i][j] == "*":
            if sign==False and arr[i][j-1] == "_" and arr[i][j+1] == "_":
                x=i+2
                y=j+1
                print(x, y)
                sign = True
                break
        if sign :
            break

left = 0
right = 0
hr = 0
ld = 0
rd = 0
for j in range(y-1):
    if arr[x-1][j] == "*":
        left+=1

for j in range(y,n):
    if arr[x-1][j] == "*":
        right+=1

for i in range(x,n):
    if arr[i][y-1] == "*":
        hr+=1

st = hr+x
for i in range(st-1,n):
    if arr[i][y-2] =="*":
        ld+=1
for i in range(st,n):
    if arr[i][y] == "*":
        rd +=1

print(left, right, hr, ld, rd)