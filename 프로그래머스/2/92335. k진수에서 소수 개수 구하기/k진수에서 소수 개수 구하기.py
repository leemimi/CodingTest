from math import sqrt
def check(x):
    if x<= 1:
        return False
    for i in range(2,int(x**(1/2)+1)):
        if x%i == 0:
            return False
    return True
        


def solution(n, k):
    answer = 0
    
    value = ''
    while n>0:
        a,b = divmod(n,k)
        n//=k
        value += str(b)
    value = value[::-1]
    
    for i in value.split('0'):
        if i.isdigit() and check(int(i)):
            answer+=1
    
    return answer