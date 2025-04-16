def solution(n, l, r):
    answer = 0
    
    def check(idx):
        while idx>=5:
            if (idx-2)%5==0:
                return False
            idx//=5
        return idx!=2
    
    
    for i in range(l-1,r):
        if check(i):
            answer+=1
    
    return answer