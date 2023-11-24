n = int(input())
dict = {}
for _ in range(n):
    s = input().split('.')
    if s[1] not in dict:
        dict[s[1]] = 1
    else:
        dict[s[1]] +=1
d = sorted(dict.items())

for k,v in d:
    print(k, v)