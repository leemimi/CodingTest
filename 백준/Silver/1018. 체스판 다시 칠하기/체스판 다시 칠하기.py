n, m = map(int, input().split())
arr = [list(map(str, input())) for _ in range(n)]

paint = []
for i in range(n-7):
    for j in range(m-7):
        board1 = 0
        board2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) %2 ==0:
                    if arr[a][b] != 'W':
                        board1+=1
                    else:
                        board2 +=1
                else:
                    if arr[a][b] !='W':
                        board2 +=1
                    else:
                        board1 +=1
        paint.append(board1)
        paint.append(board2)
print(min(paint))