from collections import deque
def solution(bridge_length, weight, truck_weights):
    time= 0
    
    road = deque([0]*bridge_length)
    truck = deque(truck_weights)
    cur = 0
    while truck:
        time+=1
        
        cur -= road.popleft()
        
        if cur + truck[0] <= weight:
            cur += truck[0]
            road.append(truck.popleft())
        else:
            road.append(0)
        
        
    if len(road):
        time += len(road)
        

    
    return time