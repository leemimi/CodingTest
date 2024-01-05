def solution(board):
    answer = 0
    boards = ''.join(board)
    cnt = boards.count('O') - boards.count('X')


    if cnt not in [0,1]:
        return 0

    colboard = list(zip(*board))
    Ocnt, Xcnt = 0,0

    for i in range(3):
        if colboard[i].count('O')==3 or board[i].count('O')==3:
            Ocnt+=1
        if colboard[i].count('X')==3 or board[i].count('X')==3:
            Xcnt+=1

    for i in range(0,3,2):
        if (board[0][i] == board[1][1] == board[2][2-i]== 'O'):
            Ocnt+=1
        if (board[0][i] == board[1][1] == board[2][2-i]== 'X'):
            Xcnt+=1

    if Ocnt and Xcnt:
        return 0
    if Ocnt and cnt==0:
        return 0
    if Xcnt and cnt>=1:
        return 0
    
    return 1