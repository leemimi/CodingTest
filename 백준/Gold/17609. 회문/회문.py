def finalCheck(p, lt, rt):
    while lt < rt:
        if p[lt] == p[rt]:
            lt+=1
            rt-=1
        else:
            return False
    return True


def check(p, lt, rt):
    if p == p[::-1]:
        return 0
    while lt<rt:
        if p[lt] == p[rt]:
            lt+=1
            rt-=1
        else:
            lc = finalCheck(p, lt+1, rt)
            rc = finalCheck(p, lt, rt-1)
            if lc or rc:
                return 1
            else:
                return 2
    return 1


T = int(input())
for _ in range(T):
    p = input()
    print(check(p,0,len(p)-1))