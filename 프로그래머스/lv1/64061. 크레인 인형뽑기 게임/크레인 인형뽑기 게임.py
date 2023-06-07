def solution(board, moves):
    answer = 0
    bucket = []
    for m in moves:
        for j in range(len(board)):
            if board[j][m-1] != 0 :
                bucket.append(board[j][m-1])
                board[j][m-1]=0
                if len(bucket)>1:
                    if bucket[-1] == bucket[-2]:
                        bucket.pop(-1)
                        bucket.pop(-1)
                        answer+=2
                break
        
        
    return answer
