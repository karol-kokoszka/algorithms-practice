from typing import List

def verify_sudoku_board(board: List[List[int]]) -> bool:
    # Go through all rows
    for i in range(len(board)):
        j = 0
        elementsInRow = {}
        while (j < len(board[i])) and (board[i][j] not in elementsInRow):
            if board[i][j] == 0:
                j = j + 1
                continue
            elementsInRow[board[i][j]] = None
            j = j + 1
        if j < len(board[i]):
            return False
    # Go through all columns
    for i in range(len(board[0])):
        j = 0
        elementsInColumn = {}
        while (j < len(board)) and (board[j][i] not in elementsInColumn):
            if board[j][i] == 0:
                j = j + 1
                continue
            elementsInColumn[board[j][i]] = None
            j = j + 1
        if j < len(board):
            return False
    # Go through all squares
    for sq in range(9):
        elementsInSquare = {}
        for row in range(3):
            for col in range(3):
                element = board[(sq // 3)*3 + row][(sq % 3) * 3 + col]
                # print(sq, row, col, element)
                if element == 0:
                    continue
                elif element not in elementsInSquare:
                    elementsInSquare[element] = None
                else:
                    return False

    return True