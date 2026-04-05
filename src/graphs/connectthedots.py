from typing import List

def connect_the_dots(points: List[List[int]]) -> int:    
    if len(points) == 0:
        return 0
    minimumCostFromTree = {}
    tree = [points[0]]
    for i in range(1, len(points)):
        minimumCostFromTree[tuple(points[i])] = abs(points[0][0] - points[i][0]) + abs(points[0][1] - points[i][1])

    sum = 0
    for i in range(1, len(points)):
        min = float('inf')
        minPoint = None
        for k in minimumCostFromTree.keys():
            if minimumCostFromTree[k] < min:
                min = minimumCostFromTree[k]
                minPoint = k

        sum += minimumCostFromTree[minPoint]
        tree.append(minPoint)
        minimumCostFromTree.pop(minPoint)   

        for k in minimumCostFromTree.keys():
            current = abs(minPoint[0] - k[0]) + abs(minPoint[1] - k[1])
            if current < minimumCostFromTree[k]:
                minimumCostFromTree[k] = current

    return sum

        
