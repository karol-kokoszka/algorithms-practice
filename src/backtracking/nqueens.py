from typing import List

"""
There is a chessboard of size n x n. 
Your goal is to place n queens on the board such that no two queens attack each other. 
Return the number of distinct configurations where this is possible.
"""
def n_queens(n: int) -> int:
    cols = {}
    diagf = {}   # diagf[(a, b)] = diagf[b - a]
    diagb = {}   # diagb[(a, b)] = diagb[b + a]

    def backtracking(current: int):
        result = 0

        if current == n: 
            return 1
        for i in range(n):
            if cols.get(i) != None or diagf.get(i - current) != None or diagb.get(i + current) != None:
                continue
            cols[i], diagf[i - current], diagb[i + current] = True, True, True
            result += backtracking(current + 1)
            cols[i], diagf[i - current], diagb[i + current] = None, None, None
        return result

    return backtracking(0)    
