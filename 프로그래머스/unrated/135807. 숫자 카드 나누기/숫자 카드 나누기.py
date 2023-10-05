def solve(a,b):
    while b!=0:
        a,b = b, a%b
    return a

def solution(arrayA, arrayB):
    
    a = arrayA[0]
    for i in range(len(arrayA)):
        a = solve(a, arrayA[i])
    
    b = arrayB[0]
    for i in range(len(arrayB)):
        b = solve(b, arrayB[i])
    
    for i in range(len(arrayA)):
        if arrayA[i]%b == 0:
            b = 1
        if arrayB[i]%a == 0:
            a = 1
    
    if a ==1 and b ==1 :
        return 0
    else:
        return max(a,b)
    