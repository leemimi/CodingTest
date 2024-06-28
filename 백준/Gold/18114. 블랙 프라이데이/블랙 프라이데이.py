import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr= list(map(int, input().split()))
arr.sort()

def search(lt, rt, diff):
    while lt<=rt:
        mid =(lt+rt)//2
        if arr[mid] == diff:
            return True
        elif arr[mid] > diff:
            rt = mid-1
        else:
            lt = mid +1
    return False

def check(n,c):
    if c in arr:
        return True

    lt, rt = 0, n-1
    while lt<rt:

        total = arr[lt] + arr[rt]
        if total == c:
            return True
        elif total > c:
            rt-=1
        else:
            diff = c - total
            if arr[lt] != diff and arr[rt] != diff and search(lt, rt, diff):
                return True
            lt+=1

if check(n,m):
    print(1)
else:
    print(0)