from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    passed_truck = []
    passing_truck = deque()
    passing_time = deque()
    truck_weights = deque(truck_weights)
    
    while truck_weights:
        
        while passing_time and passing_time[0] == answer:
            time = passing_time.popleft()
            passing_truck.popleft()
            
        if sum(passing_truck) + truck_weights[0] <= weight and len(passing_truck) <= bridge_length:
            truck = truck_weights.popleft()
            passing_time.append(answer + bridge_length)
            passing_truck.append(truck)
            
            # print(passing_time, passing_truck)
        answer += 1
        
        # print(passed_truck)
        # print(passing_time)
    return max(passing_time) + 1