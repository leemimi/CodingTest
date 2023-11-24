def solution(m, n, board):
    board = list(map(list, board))
    ans = 0
    
    while True:
        box=set()
        for i in range(m-1):
            for j in range(n-1):
                lt, ld, rt, rd =  board[i][j], board[i + 1][j], board[i][j + 1], board[i + 1][j + 1]
                
                if lt==ld==rt==rd and lt!= 0:
                    box.add((i+1,j))
                    box.add((i,j))
                    box.add((i,j+1))
                    box.add((i+1,j+1))
        if not box:
            break
        ans+=len(box)
        
        for b in box:
            x,y = b
            board[x][y] = 0
        for j in range(n):
            for i in range(m):
                for ii in range(1,m-i):
                    if board[ii][j] == 0:
                        board[ii-1][j], board[ii][j] = board[ii][j], board[ii - 1][j]
    return ans