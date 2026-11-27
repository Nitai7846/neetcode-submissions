class Solution:

    def isValid(self, i, j, m, n):
        if i<0 or i>=m:
            return False
        if j<0 or j>=n:
            return False 
        return True 
    
    def dfs(self, i, j, m, n, grid, vis):

        if not self.isValid(i,j,m,n):
            return 0
        
        if vis[i][j]:
            return 0
        
        if grid[i][j] == 0:
            return 0
        
        vis[i][j] = True
        
        return (1 + self.dfs(i-1,j,m,n,grid,vis) + self.dfs(i+1,j,m,n,grid,vis) + self.dfs(i,j-1,m,n,grid,vis) + 
        self.dfs(i,j+1,m,n,grid,vis))

    

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        m = len(grid) 
        n = len(grid[0])

        vis = [[False]*n for _ in range(m)]
        max_area = 0 
        cur_area = 0 

        for i in range(0, m):
            for j in range(0, n):
                if not vis[i][j] and grid[i][j] == 1:
                    cur_area = self.dfs(i,j,m,n,grid,vis)
                
                max_area = max(max_area, cur_area)

        return max_area 


        