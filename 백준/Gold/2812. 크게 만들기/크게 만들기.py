n,k = map(int, input().split())
arr = list(map(int, input().rstrip()))

stack = []
t = k

for i in range(n):
    while stack and k > 0 and stack[-1] < arr[i] :
        k-=1
        stack.pop()
    stack.append(arr[i])

print(''.join(list(map(str, stack[:n-t]))))