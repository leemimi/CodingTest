def solution(citations):
    citations.sort()
    cnt=0
    max=0
    for i in range(len(citations)):
        if len(citations)-i <= citations[i]:
            cnt+=1
        if max<cnt:
            max =cnt
    return max
        