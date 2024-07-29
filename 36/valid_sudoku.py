class Solution(object):
    def isValid(self, vals): 
        # valid if all numeric values are unique
        nums = [v for v in vals if v.isdigit()]
        unique_values = set(nums)
        return len(unique_values) == len(nums)

    def isValidRow(self, matrix, row):
        return self.isValid(matrix[row])
    
    def isValidColumn(self, matrix, col):
        column = [row[col] for row in matrix]
        return self.isValid(column)
    
    def isValidSquare(self, matrix, num):
        row_start = int(num / 3)*3
        col_start = int(num % 3)*3

        sq = []
        for i in range(0, 3):
            for j in range(0, 3):
                sq.append(matrix[row_start+i][col_start+j])

        return self.isValid(sq)

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # row, column, squares
        for i in range(0, 9):
            if self.isValidRow(board, i) == False:
                return False
            if self.isValidColumn(board, i) == False:
                return False
            if self.isValidSquare(board, i) == False:
                return False
            
        return True
        
solution = Solution()
print(solution.isValidSudoku(
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
))
print(solution.isValidSudoku(
    [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
))