from typing import List

def count_islands(matrix: List[List[int]]) -> int: 
    if len(matrix) == 0:
        return 0
    visited = [[0]*len(matrix[0]) for _ in range(len(matrix))]
    islands = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 and visited[i][j] != True:
                dfs(i, j, matrix, visited)
                islands += 1
    return islands

def dfs(x, y: int, matrix: List[List[int]], visited: List[List[int]]):
    if matrix[x][y] == 0 or visited[x][y]:
        return 
    visited[x][y] = True
    if x > 0:
        dfs(x - 1, y, matrix, visited)
    if x < len(matrix) - 1:
        dfs(x + 1, y, matrix, visited)
    if y > 0:
        dfs(x, y - 1, matrix, visited)
    if y < len(matrix[0]) - 1:
        dfs(x, y + 1, matrix, visited)