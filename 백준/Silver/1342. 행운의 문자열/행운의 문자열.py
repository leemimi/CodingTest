from collections import Counter
S = input()
n = len(S)
S = list(map(str, S.strip()))
cnt = Counter(S)


def dfs(L, tmp):
    answer = 0
    if L == n:
        return 1

    for i in cnt.keys():
        if i == tmp or cnt[i] == 0:
            continue
        cnt[i] -=1
        answer += dfs(L+1, i)
        cnt[i] +=1
    return answer


print(dfs(0,""))