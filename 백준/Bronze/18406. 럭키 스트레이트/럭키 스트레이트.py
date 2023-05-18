x = input()

res=0
for i in range(0,len(x)//2):
    res += int(x[i])
res2=0
for j in range(len(x)-1,len(x)//2-1,-1):
    res2 += int(x[j])


if res == res2 :
    print("LUCKY")
else:
    print("READY")