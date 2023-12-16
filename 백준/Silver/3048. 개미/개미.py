n,m =map(int,input().split())
n1 = list(input())
n2 = list(input())
t = int(input())
n1.reverse()
ants = list(n1+n2)

time = 0
new_ants = ants[:]

while time!=t:
    for i in range(len(ants)-1):
        if ants[i] in n1 and ants[i+1] in n2:
            tmp = new_ants[i]
            new_ants[i] = ants[i+1]
            new_ants[i+1] = tmp

    ants = new_ants[:]
    time+=1
print(''.join(new_ants))