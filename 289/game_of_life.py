from os import system
from sys import argv
from time import sleep
import random
from starting_seeds import *
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

    def gameOfLife(self, current_board: List[List[int]], next_board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(current_board)
        columns = len(current_board[0]) if rows > 0 else 0
        for row in range(0, rows):
            for column in range(0, columns):
                neighbor_sum = self.getNeighborSum(current_board, rows, columns, row, column)
                next_board[row][column] = self.getNextCellState(current_board[row][column], neighbor_sum)

#######################################################################################################################
def printBoard(board: List[List[int]], deadChr: str = " ", aliveChr: str = chr(0x2588)) -> None:
    s = ""
    for row in board:
        for cell in row:
            s += aliveChr if cell == 1 else deadChr
        s += "\n"
    print(s)

def padBoard(board: List[List[int]], rows: int, columns: int) -> None:
    rows_to_add = rows - len(board)
    columns_to_add = columns - len(board[0])
    
    for _ in range(rows_to_add):
        board.append([0] * len(board[0]))

    for row in board:
        row.extend([0] * columns_to_add)

    return board

def randomArray(rows: int, columns: int) -> None:
    # Create a 2D array with m rows and n columns
    array = []
    
    for _ in range(rows):
        # Fill each row with random 1s and 0s
        row = [random.choice([0, 1]) for _ in range(columns)]
        array.append(row)
        
    return array

solution = Solution()
# inputs = [
#     [[0,1,0],[0,0,1],[1,1,1],[0,0,0]],
#     [[1,1],[1,0]]
# ]
# for input in inputs:
#     solution.gameOfLife(input)
#     printBoard(input)

delay_s = float(argv[1]) if len(argv) > 1 else 0.0333
num_rows = int(argv[2]) if len(argv) > 2 else 10
num_columns = int(argv[3]) if len(argv) > 3 else 10

board = GLIDER_GUN
# board = randomArray(num_rows, num_columns)
padBoard(board, num_rows, num_columns)

buf_current = [row[:] for row in board]
buf_next = [row[:] for row in board]

while(True):
    try:
        system("clear")
        printBoard(buf_current)
        solution.gameOfLife(buf_current, buf_next)
        sleep(delay_s)
        # swap buffers
        buf_current, buf_next = buf_next, buf_current
    except KeyboardInterrupt:
        print("\nSeed")
        printBoard(board, "0", "1")
        break
