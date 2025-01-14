import sys
input = sys.stdin.readline

n,l,r,x = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
arr.sort()
def dfs(L, sums, lst):
    global answer
    if (l<=sums<=r) and (x <= abs(min(lst)- max(lst))):
        answer+=1

    for i in range(L+1,n):
        dfs(i, sums+arr[i], lst+[arr[i]])

for i in range(n):
    dfs(i,arr[i],[arr[i]])
print(answer)