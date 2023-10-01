n = int(input())
arr = list(map(int, input().split()))

maxArr = arr
minArr = arr

for i in range(n-1):
    arr = list(map(int, input().split()))

    maxArr = [arr[0]+max(maxArr[0], maxArr[1]), arr[1]+max(maxArr), arr[2]+max(maxArr[1],maxArr[2])]
    minArr = [arr[0]+min(minArr[0], minArr[1]), arr[1]+min(minArr), arr[2]+min(minArr[1],minArr[2])]


print(max(maxArr), min(minArr))
