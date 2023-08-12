n = int(input())

arr=[]
for _ in range(n):
    a = input()
    arr.append(a)

dict = {}

for word in arr:
    cnt = len(word)-1
    for w in word:
        if w not in dict:
            dict[w] = pow(10,cnt)
        else:
            dict[w] += pow(10,cnt)
        cnt -=1
dict = sorted(dict.values(), reverse=True)

res = 0
num = 9

for k in dict:
    res += k*num
    num-=1

print(res)