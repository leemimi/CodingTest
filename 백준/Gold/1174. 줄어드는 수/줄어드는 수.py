n = int(input())

cnt = 1

def dfs(cur):

    res.append(int(cur))
    for j in range(0,int(cur[-1])):
        dfs(cur+str(j))

if n > 1023:
    print(-1)

else:
    res = []

    for i in range(10):
        dfs(str(i))

    print(sorted(res)[n-1])