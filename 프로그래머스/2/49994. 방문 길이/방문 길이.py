from collections import deque
def solution(dirs):
    answer = 0
    dir = {'U': (-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}
    

    go = set()
    
    x = 0
    y = 0
    for d in dirs:
        
        nx = x + dir[d][0]
        ny = y + dir[d][1]
        print(nx, ny)
        if -5<=nx<=5 and -5<=ny<=5:
            go.add((x,y,nx,ny))
            go.add((nx,ny,x,y))
            x = nx
            y = ny
    
    return len(go)//2