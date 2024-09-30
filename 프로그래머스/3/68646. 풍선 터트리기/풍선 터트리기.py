from collections import deque
def solution(a):
    answer = 0
    
    ldp = [float('inf')]*len(a)
    ldp[0] = a[0]
    
    for i in range(1,len(a)):
        ldp[i] = min(ldp[i-1],a[i])
    
    ldp[-1] = a[-1]
    for i in range(len(a)-2,0,-1):
        if a[i] < ldp[i-1] and a[i] < ldp[i+1]:
            answer+=1
        elif (ldp[i-1] <a[i] <ldp[i+1]) or (ldp[i-1]>a[i]>ldp[i+1]):
            answer+=1
        else:
            pass
        
        ldp[i] = min(ldp[i+1],a[i])
    
    
    
    return answer+2