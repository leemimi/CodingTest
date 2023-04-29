n = int(input())
tops = list(map(int, input().split()))
stack=[]
ans = [0]*n
for i in range(0,n):
    while stack:
        if(stack[-1][0]>=tops[i]):
            ans[i] = stack[-1][1]
            break
        else:
            stack.pop()
    stack.append((tops[i],i+1))

for i in range(n):
    print(ans[i], end=' ')