from itertools import permutations
from collections import deque
def solution(expression):
    answer = 0
    
    cal = ['+', '-', '*']
    lst = list(permutations(cal,3))
    num=''
    nums = deque()
    for e in expression:
        if e.isdigit():
            num += e
        else:
            nums.append(num)
            num = ''
            nums.append(e)
    nums.append(num)
    
    res = 0 
    for l in lst:
        arr = deque(nums)
        for c in l: 
            stack = []
            while len(arr)>0:
                tmp = arr.popleft()
                if tmp == c:
                    prev = stack.pop()
                    next_num = arr.popleft()
                    res = str(eval(prev+c+next_num))
                    stack.append(res)
                else:
                    stack.append(tmp)
            arr = deque(stack)
        answer = max(answer, abs(int(arr[0])))
            
            
            
            
            
    return answer