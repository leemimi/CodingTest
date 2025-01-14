from collections import defaultdict
def solution(genres, plays):
    answer = []
    n = len(genres)
    times = defaultdict(int)
    for i in range(n):
        times[genres[i]] += plays[i]
    
    q=defaultdict(list)
    for i, (g,p) in enumerate(zip(genres, plays)):
        q[g].append([i,p])
        
    
    t = sorted(q.items(), key = lambda x:(sum(p for _, p in x[1])), reverse = True)

    for genre, play in t:
        play.sort(key = lambda x:(-x[1], x[0]))
        answer.extend([i for i, _ in play[:2]])
    
    
    return answer