T = int(input())
for _ in range(T):
    arr = input()
    pwd = []
    sub = []
    for a in arr:
        if a == '<':
            if pwd:
                sub.append(pwd.pop())
        elif a == '>':
            if sub:
                pwd.append(sub.pop())
        elif a =='-':
            if pwd:
                pwd.pop()
        else:
            pwd.append(a)
    print("".join(pwd),"".join(sub[::-1]),sep="")