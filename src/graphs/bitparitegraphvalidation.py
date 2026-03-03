from typing import List

def bipartite_graph_validation(graph: List[List[int]]) -> bool:
    if len(graph) == 0:
        return True
    visited = {}
    for node in range(len(graph)):
        if node not in visited and not dfs_color(graph, node, False, visited):
            return False
    return True

def dfs_color(graph: List[List[int]], current: int, color: bool, visited: dict) -> bool:
    visited[current] = color
    for node in graph[current]:
        if node in visited:
            if visited[node] == color:
                return False
        else:
            if not dfs_color(graph, node, not color, visited):
                return False
    return True