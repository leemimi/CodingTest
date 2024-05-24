import sys

n = int(input())
arr = list(map(int, input().split()))

def blend(prev, i, k):
    if i> k+1:
        return prev
    if i == 1:
        cnt = 2**k
    else:
        cnt = 2**(k-i+1)

    size = len(prev)
    next = prev[size-cnt:]
    return blend(next, i+1, k) + prev[:size-cnt]


card = [j+1 for j in range(n)]
def solv():
    k=1
    while 2**k < n:
        first = blend(card, 1, k)
        k2 = 1
        while 2**k2<n:
            second = blend(first, 1, k2)
            if second == arr:
                print(k, k2)
                return
            k2+=1
        k+=1

solv()