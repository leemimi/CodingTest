import math
def solution(str1, str2):
    answer = 0
    A =[]
    B =[]
    str1=str1.upper()
    str2=str2.upper()
    
    
    for i in range(len(str1)):
        a = str1[i:i+2]
        if(a.isalpha() == False or len(a)<2):
            continue
        A.append(str1[i:i+2])

    for i in range(len(str2)):
        b = str2[i:i+2]
        if(b.isalpha()==False or len(b)<2):
            continue   
        B.append(str2[i:i+2])
    
    if len(A) ==0 and len(B) ==0 :
        return 65536
    
    A_copy = A.copy()
    B_copy = B.copy()
    
    su =[]
    for i in A:
        if i in B_copy:
            su.append(i)
            A_copy.remove(i)
            B_copy.remove(i)
    
    hap = []
    hap = su + A_copy + B_copy            
    

    if len(hap) == 0 : return 65536


    answer = int((len(su)/len(hap))*65536)
    
 # ab, ba, ab와 ba, ab, ba
    return answer