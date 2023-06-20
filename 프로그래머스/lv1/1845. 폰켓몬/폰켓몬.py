def solution(nums):
    answer = 0
    w = len(set(nums))
    
    if len(nums)/2 > w:
        return w
    else:
        return int(len(nums)/2)
        