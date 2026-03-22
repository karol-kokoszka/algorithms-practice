"""
You are positioned at the top-left corner of a m x n matrix, 
and can only move downward or rightward through the matrix. 
Determine the number of unique pathways you can take 
to reach the bottom-right corner of the matrix.
"""

def matrix_pathways(m: int, n: int) -> int:
    if m == 0 or n == 0:
        return 0
    known = [[-1] * n for _ in range (m)]
    known[m - 1][n - 1] = 1

    def pathwaysFrom(x: int, y: int) -> int:   
        if known[x][y] != -1:
            return known[x][y]
        current = 0
        if x + 1 < m:
            known[x + 1][y] = pathwaysFrom(x + 1, y)
            current += known[x + 1][y]
        if y + 1 < n:
            known[x][y + 1] = pathwaysFrom(x, y + 1)
            current += known[x][y + 1]
        return current
    
    return pathwaysFrom(0, 0)

    