s = input().upper()
arr = list(set(s))

cnt = []
for i in arr:
    cnt.append(s.count(i))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(arr[cnt.index(max(cnt))])

