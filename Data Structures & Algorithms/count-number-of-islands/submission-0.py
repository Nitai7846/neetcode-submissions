class Solution:

    def isValid(self, i,j,m,n):

        if i < 0 or i>=m:
            return False
        if j<0 or j>=n:
            return False
        
        return True 


    def dfs(self, i, j, vis, grid):

        m = len(grid)
        n = len(grid[0])

        if not self.isValid(i,j,m,n):
            return 

        if grid[i][j] == '0':
            return 
        
        if vis[i][j]:
            return 

        vis[i][j] = True 

        self.dfs(i-1, j, vis, grid)
        self.dfs(i+1, j, vis, grid)
        self.dfs(i, j-1, vis, grid)
        self.dfs(i, j+1, vis, grid)
                

    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])

        vis = [[False] * n for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):

                if not vis[i][j] and grid[i][j] == "1" :
                    count += 1
                    self.dfs(i,j,vis,grid)

        return count







        