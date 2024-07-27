class Solution(object):
    def islandNodes(self, row, col, rows, cols, grid, visited):
        # from a given node, perform dfs for all '1' nodes and accumulate them
        nodes = []
        dfs = [(row, col)]
        while len(dfs) > 0:
            row, col = dfs.pop();

            if visited[row][col] == True:
                continue;
            
            visited[row][col] = True

            if grid[row][col] == '0':
                continue; 
            
            nodes.append((row,col))

            if row > 0:
                dfs.append((row-1, col))
            if row < rows-1:
                dfs.append((row+1, col))
            if col > 0:
                dfs.append((row, col-1))
            if col < cols-1:
                dfs.append((row, col+1))
        
        return nodes


    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = []
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        for i in range(0, rows):
            for j in range(0, cols):
                nodes = self.islandNodes(i, j, rows, cols, grid, visited)
                if len(nodes) > 0:
                    islands.append(nodes)
        
        return len(islands)

        
solution = Solution()
print(solution.numIslands(
    [["1","1","1","1","0"],
     ["1","1","0","1","0"],
     ["1","1","0","0","0"],
     ["0","0","0","0","0"]]
))

print(solution.numIslands(
    [["1","1","0","0","0"],
     ["1","1","0","0","0"],
     ["0","0","1","0","0"],
     ["0","0","0","1","1"]]
))

print(solution.numIslands(
    [["1","1","1"],
     ["0","1","0"],
     ["1","1","1"]])
)