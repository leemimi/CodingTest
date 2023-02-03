def solution(array, commands):
    answer = []
    arr=[]
    for x in commands:
        arr=array[x[0]-1:x[1]]
        arr.sort()
        answer.append(arr[x[2]-1])
    return answer