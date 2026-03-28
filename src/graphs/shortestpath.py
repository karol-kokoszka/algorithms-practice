from typing import List
import heapq

def shortest_path(n: int, edges: List[int], start: int) -> List[int]:
    paths, graph = {}, {}
    for i in range(n):
        paths[i] = float('inf')
        graph[i] = []
    h = []
    heapq.heappush(h, (0, start))
    paths[start] = 0
    for e in edges:
        graph[e[0]].append((e[1], e[2]))
        graph[e[1]].append((e[0], e[2]))

    while len(h) > 0:
        distance, currentNode = heapq.heappop(h)
        for e in graph[currentNode]:
            if distance + e[1] < paths[e[0]]:
                paths[e[0]] = distance + e[1]
                heapq.heappush(h, (paths[e[0]], e[0]))

    result = [-1] * n 
    for i in range(n):
        if paths[i] != float('inf'):
            result[i] = paths[i]
    return result
