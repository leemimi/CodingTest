n = int(input())

def check(p):
    m = len(p)
    for j in range(1, m//2+1):
        if p[-j:] == p[-2*j:-j]:
            return False
    return True



def dfs(L, nums):
    if L == n:
        print(nums)
        exit()

    for i in range(1,4):
        next = nums+str(i)
        if check(next):
            dfs(L+1, next)



dfs(1,'1')