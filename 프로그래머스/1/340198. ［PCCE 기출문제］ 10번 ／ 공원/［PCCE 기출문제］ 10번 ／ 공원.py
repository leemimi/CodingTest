from collections import deque
def find(x,y, m, park):
    f = True
    for k in range(m):
        nx = x+k
        for d in range(m):
            ny = y + d
            if 0>nx or nx>=len(park) or  0>ny or ny >=len(park[0]):
                f = False
                break
            elif park[nx][ny] != "-1":
                f = False
                break
        if not f:
            return False
    return True

def solution(mats, park):
    answer = 0
    vaild = set()
    for mat in mats:
    
        flag = True
        for i in range(len(park)):
            for j in range(len(park[0])):
                if park[i][j] == "-1":
                    flag = find(i,j,mat,park)
                    if flag:
                        vaild.add(mat)
                        break
                        
    if len(vaild) <=0:
        return -1
    answer = max(vaild)
    return answer