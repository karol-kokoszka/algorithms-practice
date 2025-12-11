from typing import List, Tuple

"""
Determine if a target value exists in a matrix. 
Each row of the matrix is sorted in non-decreasing order, 
and the first value of each row is greater than or 
equal to the last value of the previous row.
"""
def matrix_search(matrix: List[List[int]], target: int) -> bool:
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    pos2Matrix = make_position_in_matrix(len(matrix[0]))
    left, right = 0, len(matrix) * len(matrix[0]) - 1
    while left < right:
        mid = left + (right - left) // 2
        midMatrix = pos2Matrix(mid)
        if matrix[midMatrix[0]][midMatrix[1]] < target:
            left = left + 1
        else:
            right = mid
    leftMatrix = pos2Matrix(left)
    return matrix[leftMatrix[0]][leftMatrix[1]] == target

def make_position_in_matrix(lenX: int):
    def position_in_matrix(pos: int) -> Tuple[int, int]:
        return (pos // lenX, pos % lenX)
    return position_in_matrix