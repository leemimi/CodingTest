def solution(citations):
    citations.sort()
    print(citations)
    cnt=0
    for idx,num in enumerate(citations):
        if(idx >= num):
            cnt+=1
    return len(citations)-cnt+1