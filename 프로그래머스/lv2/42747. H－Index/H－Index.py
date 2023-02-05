def solution(citations):
    citations.sort()
    cnt=0
    max=0
    for i in range(len(citations)):
        if len(citations)-i <= citations[i]:
            print(cnt, end=' ')
            print(i)
            print('--------------')
            cnt+=1
            print(cnt)
        if max<cnt:
            max =cnt
    return cnt
        