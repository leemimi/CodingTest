n = int(input())
arr = list(map(int, input().split()))

stack = []
answer = [0]*n
for i in range(n):
    while stack:
        if arr[i] <= stack[-1][0]:
            answer[i] = stack[-1][1]
            break
        else:
            stack.pop()
    stack.append((arr[i], i+1))
print(*answer)