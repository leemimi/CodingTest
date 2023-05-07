def bt(row,queen,n):
    cnt = 0
    if row == n:
        return 1
    for col in range(n):
        queen[row] = col
        
        for x in range(row):
            if queen[x] == queen[row]:
                break
            if abs(queen[x]-queen[row])==(row-x):
                break
        else:
            cnt +=bt(row+1,queen,n)
    return cnt
        
    
def solution(n):
    return bt(0,[0]*n,n)