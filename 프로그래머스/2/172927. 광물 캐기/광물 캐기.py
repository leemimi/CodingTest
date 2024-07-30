def solution(picks, minerals):
    ans = []
    weapons ={
        'diamond':0, 'iron':1, 'stone':2
    }
    rate = [[1,1,1],
           [5,1,1],
           [25,5,1]]
    
    def dfs(minerals, picks, p):
        if sum(picks) == 0 or minerals ==[]:
            ans.append(p)
            return
        m = minerals[:5]
        for i in range(3):
            if picks[i] >0:
                picks[i]-=1
                val = calculate(i,m)
                dfs(minerals[5:], picks, p+val)
                picks[i]+=1

    def calculate(idx, minerals):
        tr = 0
        for m in minerals:
            tr += rate[idx][weapons[m]]
        return tr
    dfs(minerals, picks, 0)
    ans.sort()
        
    return ans[0]