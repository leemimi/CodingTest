from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    
    currentWeight=0
    while len(truck_weights)!=0:
        answer+=1

        currentWeight -= bridge.popleft()

        if currentWeight + truck_weights[0] <= weight:
            currentWeight+= truck_weights[0]
            bridge.append(truck_weights.popleft())

        else: 
            bridge.append(0)
            
    answer += bridge_length
    
    return answer