from typing import List, Tuple
from collections import deque

def matrix_infection(matrix: List[List[int]]) -> int:
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0

    maximum = -1
    q = deque()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 2:
                q.append((i, j, 0))

    maximum = max(maximum, bfs_infection(q, matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                return -1

    return maximum

def bfs_infection(q: List[Tuple[int, int, int]], matrix: List[List[int]]) -> int:
    visited = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    maximum = -1
    while q:
        pos = q.popleft()
        x, y, steps = pos[0], pos[1], pos[2]
        if visited[x][y]:
            continue
        visited[x][y] = True
        matrix[x][y] = 2
        maximum = max(maximum, steps)
        if x > 0 and matrix[x - 1][y] == 1 and visited[x - 1][y] != True:
            q.append((x - 1, y, steps + 1))
        if x < len(matrix) - 1 and matrix[x + 1][y] == 1 and visited[x + 1][y] != True:
            q.append((x + 1, y, steps + 1))
        if y > 0 and matrix[x][y - 1] == 1 and visited[x][y - 1] != True:
            q.append((x, y - 1, steps + 1))
        if y < len(matrix[0]) - 1 and matrix[x][y + 1] == 1 and visited[x][y + 1] != True:
            q.append((x, y + 1, steps + 1))
    return maximum
