s = input()
at = [False] * len(s)

def solve(s, isActivate):
    r = ''
    for i in range(len(isActivate)):
        if isActivate[i]:
            r += s[i]
    return r


for i in range(len(s)):
    tmp = []


    for j in range(len(at)):
        if not at[j]:
            at[j] = True
            tmp.append((solve(s, at), j))
            at[j] = False

    tmp.sort()
    print(tmp[0][0])
    at[tmp[0][1]]= True