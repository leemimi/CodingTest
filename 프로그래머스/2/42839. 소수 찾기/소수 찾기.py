from itertools import permutations
import math
def solution(numbers):
    answer = 0
    arr = []
    dict = set()
    def is_prime(n):
        for i in range(2, int(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True
    def solve(arr):
        cnt = 0
        for ar in arr:
            for a in ar:
                c = int(''.join(a))
                dict.add(c)
        for d in dict:
            if d >= 2:
                flag= is_prime(d)
                if flag:
                    cnt+=1
        return cnt

    
    for i in range(1,len(numbers)+1):
        c = list(permutations(numbers,i))
        
        arr.append(c)
    
    
    answer = solve(arr)
    return answer