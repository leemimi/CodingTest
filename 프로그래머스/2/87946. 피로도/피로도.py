from itertools import permutations
def solution(k, dungeons):
    answer = 0
    
    for o in permutations(dungeons,len(dungeons)):
        hp = k
        cnt = 0
        for p in o:
            if hp>=p[0]:
                hp -= p[1]
                cnt+=1
            
            if cnt > answer:
                answer = cnt

    
    
    return answer