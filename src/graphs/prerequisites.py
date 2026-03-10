from typing import List
from collections import defaultdict

def prerequisites(n: int, prerequisites: List[List[int]]) -> bool:
    nodes = {}
    for i in range(n):
        nodes[i] = set()
    for dependencies in prerequisites:
        nodes[dependencies[0]].add(dependencies[1])

    visited = defaultdict(int)
    for node in nodes:
        if visited[node] == 0:
            visited[node] = 1
            if not dfs_no_cycle(nodes, node, visited):
               return False
            visited[node] = 2
    return True
 
def dfs_no_cycle(graph: dict, node: int, visited: dict) -> bool:
    for n in graph[node]:
        if visited[n] == 1:
            return False
        if visited[n] == 0:
            visited[n] = 1
            if not dfs_no_cycle(graph, n, visited):
                return False
            visited[n] = 2
    return True