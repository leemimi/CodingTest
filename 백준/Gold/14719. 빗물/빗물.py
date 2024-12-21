h,w = map(int, input().split())
arr = list(map(int, input().split()))

stack = []
volume = 0

for i in range(w):
    while stack and arr[i] > arr[stack[-1]]:
        top = stack.pop()
        if not len(stack):
            break
        distance = i - stack[-1] -1
        waters = min(arr[i], arr[stack[-1]])-arr[top]
        volume += distance*waters

    stack.append(i)
print(volume)