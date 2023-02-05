def solution(citations):
    citations.sort()
    cnt=0
    for i in range(len(citations)):
        if len(citations)-i <= citations[i]:
            cnt+=1
    return cnt
        