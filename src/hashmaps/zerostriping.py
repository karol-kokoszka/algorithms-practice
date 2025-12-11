from typing import List

def zero_striping(matrix: List[List[int]]) -> None:
    cols = {}
    rows = {}
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 0:
                cols[c] = None
                rows[r] = None
    for r in rows:
        for i in range(len(matrix[r])):
            matrix[r][i] = 0
    for c in cols:
        for i in range(len(matrix)):
            matrix[i][c] = 0