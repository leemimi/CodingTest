def solution(diffs, times, limit):
    answer = 0
    n = len(times)

    lt = 1
    rt = max(diffs)

    while lt<rt:
        mid = (lt+rt)//2
        
        cur =0 
        for i in range(n):
            if(mid >= diffs[i]):
                cur += times[i]
            else:
                if(i<=0):
                    cur += times[i]*(diffs[i]-mid)+times[i]
                else:
                    cur += (times[i]+times[i-1])*(diffs[i]-mid)+times[i]
        
        if(cur<=limit):
            rt = mid
        else:
            lt = mid+1
            

    return lt