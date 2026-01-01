n = int(input())
arr = []
for i in range(n):
    arr.append(input().split())

for i in range(n):
    print(f'Case #{i + 1}:', end=" ")
    for j in range(len(arr[i])):
        print(arr[i].pop(), end=" ")
    print()