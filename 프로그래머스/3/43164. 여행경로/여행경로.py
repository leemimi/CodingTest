from collections import deque
from collections import defaultdict

def solution(tickets):
    answer = []
    dic = defaultdict(list)
    for [a,b] in tickets:
        dic[a].append(b)
    print(dic)
    
    for key in dic.keys():
        dic[key].sort(reverse=True)
    print(dic)
    
    stack = ["ICN"]
    path =[]
    
    while stack:
        top = stack[-1]
        
        if not dic[top] or len(dic[top])==0:
            path.append(stack.pop())
        else:
            stack.append(dic[top].pop())
            
        print(path)
    return path[::-1]

            