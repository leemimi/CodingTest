import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def recur(idx, S, B, use):
    global answer
    if idx == n:
        if use == 0:
            return
        answer = min(abs(S-B), answer)
        return
    recur(idx+1, S*arr[idx][0],B+arr[idx][1], use+1)
    recur(idx+1, S,B, use)


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 1 << 100

recur(0,1,0,0)
print(answer)