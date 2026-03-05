from typing import List

def longest_increasing_path(matrix: List[List[int]]) -> int:
    result = 0
    longestFromPosition =  [[0] * len(matrix[0]) for _ in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            longest = longestFromPosition[i][j]
            if longest == 0:
                longest = dfs_longest(matrix, i, j, longestFromPosition)
            result = max(result, longest)
            
    return result

def dfs_longest(matrix: List[List[int]], x, y, longestFromPosition: List[List[int]]) -> int:
    l, r, u, d = 0, 0, 0, 0
    if x > 0 and matrix[x - 1][y] > matrix[x][y]:
        u = longestFromPosition[x - 1][y]
        if u == 0:
            u = dfs_longest(matrix, x - 1, y, longestFromPosition)
    if x < len(matrix) - 1 and matrix[x + 1][y] > matrix[x][y]:
        d = longestFromPosition[x + 1][y]
        if d == 0:
            d = dfs_longest(matrix, x + 1, y, longestFromPosition)
    if y > 0 and matrix[x][y - 1] > matrix[x][y]:
        l = longestFromPosition[x][y - 1]
        if l == 0:
            l = dfs_longest(matrix, x, y - 1, longestFromPosition)
    if y < len(matrix[0]) - 1 and matrix[x][y + 1] > matrix[x][y]:
        r = longestFromPosition[x][y + 1]
        if r == 0:
            r = dfs_longest(matrix, x, y + 1, longestFromPosition)
    longestFromPosition[x][y] = max(l, r, d, u) + 1
    return longestFromPosition[x][y]