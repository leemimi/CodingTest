
n = int(input())
arr = [list(map(int, input().split()))for _ in range(n)]
res =[0]*3

def check(x,y,size):
    global arr
    num = arr[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if arr[i][j] != num:
                return False
    return True

def divide(x,y,size):
    global arr, res
    if check(x,y,size):
        res[arr[x][y]+1] +=1
    else:
        ns = size//3
        for i in range(3):
            for j in range(3):
                divide(x+ns*i, y+ns*j, ns)

divide(0,0,n)
print(res[0])
print(res[1])
print(res[2])