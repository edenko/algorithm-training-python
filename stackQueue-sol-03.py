# 스택/큐 - 다리를 지나는 트럭
from collections import deque

# def solution(bridge_length = 2, weight = 10, truck_weights = [7, 4, 5, 6]):
def solution(bridge_length = 100, weight = 100, truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]):
    bridge = deque(0 for i in range(bridge_length))
    total_weight = 0
    step = 0
    truck_weights.reverse()

    while (truck_weights):
        total_weight -= bridge.popleft()
        target = truck_weights[-1]

        if (total_weight + target > weight):
            bridge.append(0)

        else:
            truck_weights.pop()
            bridge.append(target)
            total_weight += target

        step += 1

    step += bridge_length
    return step
