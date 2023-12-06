s = input()
t = input()

ans = 0
def find(t):
    if len(s) == len(t):
        return t == s
    if t[0] == 'B' and find(t[:0:-1]):
        return True
    if t[-1] == 'A' and find(t[:-1]):
        return True
print(1 if find(t) else 0)