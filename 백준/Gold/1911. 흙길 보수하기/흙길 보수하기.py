
import sys
input = sys.stdin.readline

n,l = map(int,input().split())
#이차원 배열에 데이터 입력
puddles=[(list(map(int,input().split()))) for _ in range(n)]
#puddels[0][]기준으로 오름차순 정렬
puddles.sort(key=lambda x : x[0])
result=0
boundary=puddles[0][0]
for start, end in puddles:
    if start>boundary:
        boundary=start
    diff = end-boundary
    if diff%l == 0:
        count=diff//l
        boundary=end
    else:
        count=diff//l+1
        boundary=end+(l-diff%l)
    result+=count
print(result)