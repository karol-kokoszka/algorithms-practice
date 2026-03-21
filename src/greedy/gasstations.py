from typing import List

def gas_stations(gas: List[int], cost: List[int]) -> int:
    delta = []
    sum = 0
    for i in range(len(gas)):
        delta.append(gas[i] - cost[i])
        sum+= delta[i]
    if sum < 0:
        return -1
    startPoint, sum = 0, 0
    for i in range(len(delta)):
        sum += delta[i]
        if sum < 0:
            startPoint = i + 1
            sum = 0
    return startPoint 