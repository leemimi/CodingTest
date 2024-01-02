import math
def find(num):
    if num == 1:
        return False
    for j in range(2, int(math.sqrt(num))+1):
        if num%j == 0:
            return False
    return True

T = int(input())
for _ in range(T):
    num = int(input())

    a,b = num//2, num//2
    while a>0:
        if find(a) and find(b):
            print(a, b)
            break
        else:
            a-=1
            b+=1