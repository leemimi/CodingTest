import string
import sys
s = list(map(str, input().rstrip()))
q= int(input())
count = {}
for char in string.ascii_lowercase:
    count[char] = [0]
    cnt = 0
    for i in range(len(s)):
        if s[i] == char:
            cnt +=1
        count[char].append(cnt)
for _ in range(q):
    num, l,r = map(str, input().split())
    l = int(l)
    r = int(r)

    print(count[num][r+1]- count[num][l])