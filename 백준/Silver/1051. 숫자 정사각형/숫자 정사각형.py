def solve(k):
    for i in range(n-k+1):
        for j in range(m-k+1):
            if arr[i][j] == arr[i][j+k-1] == arr[i+k-1][j] == arr[i+k-1][j+k-1]:
                return True
    return False

n,m = map(int,input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]
size = min(n,m)
for i in range(size,0,-1):
    if solve(i):
        print(i**2)
        break