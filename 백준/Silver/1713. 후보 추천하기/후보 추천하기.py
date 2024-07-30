import sys
input = sys.stdin.readline
from collections import defaultdict
n = int(input())
count = int(input())
arr = list(map(int, input().split()))

photo = []
cnt = defaultdict(int)


for i in range(count):
    if arr[i] not in cnt:
        cnt[arr[i]] = 0
    if arr[i] not in photo:
        if len(photo) < n:
            photo.append(arr[i])
            cnt[arr[i]] +=1
        elif len(photo) == n:
            c=0
            min_cnt = count+1
            id = []
            val = 0
            for a,b in cnt.items():
                if a in photo :
                    if min_cnt > b:
                        min_cnt = b
                        if len(id)>0:
                            while id:
                                id.pop()
                        id.append(a)
                    elif min_cnt == b:
                        id.append(a)

                elif a not in photo:
                    continue
            if len(id) == 1:
                v = id.pop()
                photo.remove(v)
                cnt[v] = 0
                photo.append(arr[i])
                cnt[arr[i]] +=1
            elif len(id)>1:
                min_idx = count+1
                ix = -1
                for j in id:
                    if min_idx > photo.index(j):
                        min_idx = photo.index(j)
                        ix = j
                photo.pop(min_idx)
                cnt[ix] = 0
                photo.append(arr[i])
                cnt[arr[i]] +=1
    else:
        cnt[arr[i]] +=1
    # print(photo)
    # print(cnt)
photo.sort()
print(*photo)