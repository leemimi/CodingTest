n = int(input())
arr = [int(input()) for i in range(n)]

stack=[]
sum =0

for i in range(n):
    while stack and stack[-1]<=arr[i]:
            stack.pop()
    sum+=len(stack)
    stack.append(arr[i])


print(sum)