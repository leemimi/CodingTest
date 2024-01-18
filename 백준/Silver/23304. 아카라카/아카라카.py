import sys
input = sys.stdin.readline
s = input().rstrip()

def is_pelindrome(ss):
    if ss == ss[::-1]: return True
    return False
def solve(s):
    global res
    if len(s) == 1:
        return s
    
    t = int(len(s) / 2)
    if len(s)%2==0:
        a = s[:t]
        b = s[t:]
    else:
        a = s[:t]
        b = s[t+1:]

    if a!=b:
        res = False
    elif not is_pelindrome(s):
        res = False
    elif not is_pelindrome(solve(b)):
        res = False

    return s

res = True
solve(s)
print("AKARAKA" if res else "IPSELENTI")