from collections import defaultdict
n = int(input())
arr = list(map(str,input().rstrip()))

lt = 0
rt = 0

dict = defaultdict(int)

answer = 0
while rt < len(arr):
    
    dict[arr[rt]] += 1
    

    while len(dict) > n:
        dict[arr[lt]] -= 1
        if dict[arr[lt]] == 0:
            del dict[arr[lt]]
        lt += 1

    answer = max(answer, rt - lt + 1)
    rt +=1

print(answer)