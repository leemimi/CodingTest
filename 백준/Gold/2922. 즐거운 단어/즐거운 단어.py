
s = input()
mo = {'a', 'i', 'e', 'o', 'u'}

s = s.lower()

def check(w):
    if 'l' not in w:
        return False
    for i in range(1, len(w)-1):
        if w[i] in mo and w[i+1] in mo and w[i-1] in mo:
            return False
        if w[i] not in mo and w[i+1] not in mo and w[i-1] not in mo:
            return False
    return True


def dfs(s, idx, word):
    global ans
    if '_' not in s:
        if check(s):
            tmp = 1
            for y in word:
                if y =='a':
                    tmp *=5
                elif y =='b':
                    tmp *=20
                else:
                    tmp *=1
            ans +=tmp
        return
    for i in range(idx, len(s)):
        if s[i] == '_':
            s = s[:i] + 'a' + s[i+1:]
            dfs(s, idx+1, word+'a')
            s = s[:i] + 'b' + s[i + 1:]
            dfs(s, idx + 1, word + 'b')
            s = s[:i] + 'l' + s[i + 1:]
            dfs(s, idx + 1, word + 'l')
            return

ans = 0
flag = False
for i in range(len(s)):
    if s[i] == '_':
        flag = True
        dfs(s,i,'')
        break
if not flag:
    ans = 1
print(ans)