def solution(bridge_length, weight, truck_weights):
    truck_pass = []
    time = 0
    for truck in truck_weights:
        # 무게 검사
        if weight - sum(truck_pass) > truck:
            # 다리에 트럭 추가
            truck_pass.append(truck)
            time += 1
        else:
            time += bridge_length
            truck_pass.pop(0)
        print(truck_pass)
    return time
print(solution(2,10,[7,4,5,6]))