s = input()

def dfs(idx, arr):
    if idx == len(s):
        print(*arr)
        exit()
    num1 = int(s[idx])
    if not visited[num1]:
        visited[num1] = True
        arr.append(num1)
        dfs(idx+1, arr)
        visited[num1] = False
        arr.pop()

    if idx+1 < len(s):
        num2 = int(s[idx:idx+2])
        if num2 <= n and not visited[num2]:
            visited[num2] = True
            arr.append(num2)
            dfs(idx+2,arr)
            visited[num2] = False
            arr.pop()


n = len(s) if len(s) <= 9 else 9 + (len(s) - 9) // 2
visited = [0 for _ in range(n+1)]

dfs(0,[])