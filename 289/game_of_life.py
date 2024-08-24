from typing import List

class Solution:
    def getNeighborSum(self, board: List[List[int]], rows: int, columns: int, row: int, column: int) -> int:
        sum = 0

        row_range = ( max(0, row-1), min(rows-1, row+1) )
        column_range = ( max(0, column-1), min(columns-1, column+1) )
        for i in range(row_range[0], row_range[1]+1):
            for j in range(column_range[0], column_range[1]+1):
                # skip central cell
                if i == row and j == column:
                    continue

                sum += board[i][j]

        return sum

    def getNextCellState(self, prev_state, neighbor_sum):
        if prev_state == 1 and 2 <= neighbor_sum <= 3:
            # Any live cell with two or three live neighbors lives on to the next generation
            return 1
        elif prev_state == 0 and neighbor_sum == 3:
            # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction
            return 1
            
        return 0 

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # copy current board to buffer
        prev_board = [row[:] for row in board]

        rows = len(prev_board)
        columns = len(prev_board[0]) if rows > 0 else 0
        for row in range(0, rows):
            for column in range(0, columns):
                neighbor_sum = self.getNeighborSum(prev_board, rows, columns, row, column)
                board[row][column] = self.getNextCellState(prev_board[row][column], neighbor_sum)

def printBoard(board: List[List[int]]) -> None:
    s = ""
    for row in board:
        for cell in row:
            s += str(cell) + " "
        s += "\n"
    print(s)

solution = Solution()
inputs = [
    [[0,1,0],[0,0,1],[1,1,1],[0,0,0]],
    [[1,1],[1,0]]
]
for input in inputs:
    solution.gameOfLife(input)
    printBoard(input)