import sys
from collections import defaultdict
input = sys.stdin.readline

def word(w,k):
    if k == 1:
        return 1, 1
    else:
        a = len(w)
        min_num = a
        max_num = 0
        words = defaultdict(list)
        for j in range(a):
            if w.count(w[j]) >= k:
                words[w[j]].append(j)

        if not words:
            return -1,

        for z in words.values():
            for y in range(len(z)-k+1):
                len_ = z[y+k-1] - z[y] +1
                if max_num < len_:
                    max_num = len_
                if min_num > len_:
                    min_num = len_

        return min_num, max_num
T = int(input())
for i in range(T):
    W = input()
    K = int(input())
    print(*word(W,K))