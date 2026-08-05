class Solution:
    def isValid(self, i, j, rows, cols):
        if i<0 or i>=rows:
            return False
        if j<0 or j>=cols:
            return False 
        return True 

    def dfs(self, i, j, rows, cols, grid, vis):

        if not self.isValid(i, j, rows, cols):
            return 
        
        if vis[i][j]:
            return 
        
        if grid[i][j] == '0':
            return 
        
        vis[i][j] = True 

        self.dfs(i-1, j, rows, cols, grid, vis)
        self.dfs(i+1, j, rows, cols, grid, vis)
        self.dfs(i, j-1, rows, cols, grid, vis)
        self.dfs(i, j+1, rows, cols, grid, vis)

    

    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        count = 0 

        vis = [[False]*cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if not vis[row][col] and grid[row][col] == "1":
                    count+=1
                    self.dfs(row, col, rows, cols, grid, vis)
                    
        
        return count 

        

        