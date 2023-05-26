n,d,k,c = map(int,input().split())

belt=[]
for _ in range(n):
    belt.append(int(input()))
max_num = 0

for i in range(n):
    if i+k >n:
        type = len(set(belt[i:n]+belt[:(i+k)%n]+[c]))
    else:
        type=len(set(belt[i:i+k] +[c]))
    if max_num < type:
        max_num = type

print(max_num)