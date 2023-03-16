def solution(order):
    answer = 0
    stack = []

    now = 0
    for i in range(1,len(order)+1):
        if(i != order[now]):
            stack.append(i)
        elif(i == order[now]) :
            answer+=1
            now+=1;

        if(len(stack)>0 and stack[-1]==order[now]):
            answer+=1
            stack.pop()
            now+=1;
    
    while True:
        if(len(stack)>0 and stack[-1] ==order[now]):
            answer+=1
            stack.pop()
            now+=1
        else:
            break;

    return answer