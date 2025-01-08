n,C = map(int, input().split())
strs = sorted(list(map(str, input().split())))
mo = set('aieou')
arr = []
def check(a):
    k =0
    for j in range(n):
        if a[j] in mo:
            k+=1
    if k>=1 and len(a) - k>=2:
        return True
    return False


def dfs(L, keys):
    if len(keys) == n:
        if check(keys):
            arr.append((keys))
        return

    for i in range(L, C):  # start부터 탐색
        dfs(i + 1, keys + strs[i])

dfs(0,'')
arr.sort()
for a in arr:
    print(a)