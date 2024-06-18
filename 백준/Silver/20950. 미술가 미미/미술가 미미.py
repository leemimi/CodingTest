
 

n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]
R, G, B = map(int, input().split())
new_R, new_G, new_B = 0, 0, 0
ans = 987654321

def go(x, num):
    global ans, new_R, new_G, new_B
    if num >= 2: 
        ans = min(ans, abs(new_R // num - R) + abs(new_G // num - G) + abs(new_B // num - B))
    for i in range(x+1, n):
        new_R, new_G, new_B = new_R + arr[i][0], new_G + arr[i][1], new_B + arr[i][2]
        if num < 7: 
            go(i, num + 1)
        new_R, new_G, new_B = new_R - arr[i][0], new_G - arr[i][1], new_B - arr[i][2]
go(-1, 0)
print(ans)