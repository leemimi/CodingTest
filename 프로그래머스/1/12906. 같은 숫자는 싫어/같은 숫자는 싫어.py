def solution(arr):
    answer = []
    bf = arr[0]
    cnt = 1
    for i in range(1,len(arr)):
        if bf != arr[i]:
            answer.append(bf)
            bf = arr[i]
        if i == len(arr)-1:
            answer.append(arr[i])
        
            
    return answer