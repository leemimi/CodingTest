def solution(n, results):
    answer =0
    dis = [[0] * n for _ in range(n)]
    for a,b in results:
        dis[a-1][b-1] = 1
        dis[b-1][a-1] = -1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dis[i][j] == 0:
                    if dis[i][k] ==1 and dis[k][j] ==1 : dis[i][j] =1
                    elif dis[i][k] ==-1 and dis[k][j] == -1 : dis[i][j] = -1
    for row in dis:
        if row.count(0) == 1:
            answer +=1
                    
    return answer