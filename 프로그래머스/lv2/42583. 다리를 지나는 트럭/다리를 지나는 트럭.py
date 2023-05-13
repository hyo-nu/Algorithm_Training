from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    
    second = total_w = 0
    while total_w or truck:
        land = bridge.popleft()
        if land: 
            total_w -= land
        
        if truck and total_w + truck[0] <= weight: 
            now_truck = truck.popleft() 
            total_w += now_truck
            bridge.append(now_truck)
            second += 1
        else:
            bridge.append(0)
            second += 1  
    return second
    