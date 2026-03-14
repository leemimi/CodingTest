H,S = map(int, input().split())

if H <= 2:
    print(1)
elif H <= 4:
    print(2+S)
else:
    hp = (H+1) //2
    if hp%2 == 1:
        print(hp + (3*S) //2 )
    else:
        print(hp + (3*S+1)//2)