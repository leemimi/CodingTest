import sys
input = sys.stdin.readline
n,k = map(int, input().split())

def check(a):
    return (a+1)*(n-a+1)

lt = 0
rt = n//2+1
flag = True
while lt!=rt:

    mid = (lt+rt)//2
    piece = check(mid)

    if piece > k:
        rt = mid
    elif piece == k:
        print("YES")
        sys.exit(0)
    else:
        lt = mid+1
    
print("NO")


