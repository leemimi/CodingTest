phone = ["abc","def","ghi","jkl","mno", "pqrs","tuv","wxyz"]

arr = list(map(int, input().split()))
alp = input().strip()

orphone = {}
for p in range(1,10):
    ori = arr[p-1]
    orphone[ori] = p

ans = []
prev = None
for ch in alp:
    for j, group in enumerate(phone):
        if ch in group:
            key = j+2
            press = group.index(ch)+1
            break
    pkey = orphone[key]

    if prev == pkey:
        ans.append('#')
    ans.append(str(pkey)*press)
    prev = pkey
print(''.join(ans))