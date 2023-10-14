import sys
input = sys.stdin.readline

n = int(input())
word = input().strip()
arr = [input().strip() for _ in range(n-1)]
res = 0
for a in arr:
    if abs(len(word)-len(a)) > 1 or len(set(word).difference(set(a))) > 1:
        continue
    for t in word:
        if t in a:
            a = a.replace(t,"",1)
    if len(a) <=1:
        res+=1
print(res)