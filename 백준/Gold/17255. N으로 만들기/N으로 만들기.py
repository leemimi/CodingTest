N = input()
n = list(N)


visited = dict()
ans = 0

def dfs(word, left, right, seq):
    global ans
    if word == N and seq not in visited:
        visited[seq] = 0
        ans+=1
    else:
        if left>0:
            dfs(n[left-1]+word, left -1, right, seq+word)
        if right < len(n)-1:
            dfs(word+n[right+1],left, right+1, seq+word)

for i in range(len(n)):
    dfs(n[i], i, i, n[i])

print(ans)