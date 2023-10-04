def solution(dirs):
    dir = ['U','D','R','L']
    answer = 0
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    ans = set()
    x,y = 0,0
    
    for d in dirs:
        nx=x + dx[dir.index(d)]
        ny=y + dy[dir.index(d)]
        if -5<=nx<=5 and -5<=ny<=5:
            ans.add((x,y,nx,ny))
            ans.add((nx,ny,x,y))
            x = nx
            y = ny
            
    
    return len(ans)//2