import sys

m = int(sys.stdin.readline())

S = set()
for _ in range(m):
    w = sys.stdin.readline().strip().split()
    if len(w) == 1:
        if w[0] == "all":
            S = set([i for i in range(1,21)])
        else:
            S = set()
    else:
        w, c = w[0], w[1]
        c = int(c)
        if w == 'add':
            S.add(c)
        elif w == 'remove':
            S.discard(c)
        elif w == 'check':
            if c in S:
                print(1)
            else:
                print(0)
        elif w=='toggle':
            if c in S:
                S.discard(c)
            else:
                S.add(c)
