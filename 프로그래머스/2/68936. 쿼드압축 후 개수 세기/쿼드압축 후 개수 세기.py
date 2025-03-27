def devide(lst, x,y,n):
    
    for i in range(x,x+n):
        for j in range(y,y+n):
            if lst[i][j] != lst[x][y]:
                n//=2
                devide(lst,x,y,n)
                devide(lst,x+n,y,n)
                devide(lst,x,y+n,n)
                devide(lst,x+n,y+n,n)
                return
    answer[lst[x][y]]+=1
            
def solution(arr):
    global answer
    answer = [0,0]
    n = len(arr)
    devide(arr, 0,0, n)
    
    
    
    return answer