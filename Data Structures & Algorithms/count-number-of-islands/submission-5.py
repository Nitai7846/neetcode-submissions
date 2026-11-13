class Solution:

    def isValid(self, i, j, m, n):

        if i<0 or i>=m:
            return False 
        if j<0 or j>=n:
            return False
        return True 
    
    def dfs(self, i, j, m, n ,vis, grid):

        if not self.isValid(i,j,m,n):
            return 
        
        if vis[i][j]:
            return 
        
        if grid[i][j] == '0':
            return 
        
        vis[i][j] = True 

        self.dfs(i+1,j,m,n,vis,grid)
        self.dfs(i-1,j,m,n,vis,grid)
        self.dfs(i,j-1,m,n,vis,grid)
        self.dfs(i,j+1,m,n,vis,grid)
        

    def numIslands(self, grid: List[List[str]]) -> int:


        m = len(grid)
        n = len(grid[0])
        count = 0
        vis = [[False]*n for _ in range(m)]

        for i in range(0, m):
            for j in range(0 ,n):
                if not vis[i][j] and grid[i][j] == '1':
                    count+=1
                    self.dfs(i,j,m,n,vis,grid)

        return count
        

