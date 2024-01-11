import heapq

T = int(input())
for _ in range(T):
    k = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    heapq.heapify(arr)
    ans = 0
    while len(arr)>1:
        tmp = 0
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        tmp += a+b
        ans += tmp
        heapq.heappush(arr,tmp)

    print(ans)