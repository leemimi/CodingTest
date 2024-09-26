def solution(n, t, m, p):
    answer = ''
    ans = ''
    def find(num, base):
        tmp = "0123456789ABCDEF"
        q,r = divmod(num,base)
        
        if q == 0:
            return tmp[r]
        else:
            return find(q,base) + tmp[r]
    j = 0
    while len(ans) <t*m:
        ans += str(find(j,n))
        j+=1
        
    for i in range(p-1,t*m,m):
        answer += ans[i]
                 
    
    print(answer)

            
    
    
    
    return answer

