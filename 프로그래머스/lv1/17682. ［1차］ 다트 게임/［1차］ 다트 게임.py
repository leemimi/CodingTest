import math
def solution(dartResult):
    answer = 0
    
    nums=[]
    dartResult = dartResult.replace("10", "A")
    for s in dartResult:
        if s.isdigit() or s == 'A':
            nums.append(10 if s=='A' else int(s))
        elif s.isalpha():
            if s == 'S':
                 nums[-1]=int(math.pow(nums[-1],1))
            elif s == 'D':
                nums[-1]=int(math.pow(nums[-1],2))
            else:
                nums[-1]=int(math.pow(nums[-1],3))
        else:
            if s == '*':
                if len(nums)>1:
                    nums[-1]=nums[-1]*2
                    nums[-2] = nums[-2]*2
                else:
                    nums[-1]=nums[-1]*2
            else:
                nums[-1] = nums[-1]*(-1)
    print(nums)
    answer = sum(nums)
                    
                
    return answer