def solution(n, m):
    answer = []
    result = 0
    def gcd(n,m):
        if m==0:
            return n
        return gcd(m, n%m)
    answer.append(gcd(n,m))
    def lcm(n,m):
        result = (n*m)//gcd(n,m)
        return result
    answer.append(lcm(n,m))
    
    return answer