def solution(elements):
    answer = 0
    n = len(elements)
    ans = set()
    elements = elements*2
    for i in range(1, n+1):
        for j in range(n):
            s = sum(elements[i:j+i])
            ans.add(s)
            
            
    return len(ans)