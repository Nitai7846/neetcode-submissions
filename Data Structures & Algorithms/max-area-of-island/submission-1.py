class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        max_area = 0 
        vis = [[False]*n for _ in range(m)]

        def isValid(i,j,m,n):
            if i<0 or i>=m:
                return False 
            if j<0 or j>=n:
                return False 
            return True 
        
        def dfs(i,j,vis):

            if not isValid(i,j,m,n):
                return 0

            if vis[i][j]:
                return 0
            
            if grid[i][j] == 0:
                return 0
            
            vis[i][j] = True 

            return (1 + dfs(i+1, j, vis)  +
            dfs(i-1, j, vis) +
            dfs(i, j+1, vis) +
            dfs(i, j-1, vis))

        area = 0
        for i in range(0, m):
            for j in range(0, n):
                if not vis[i][j] and grid[i][j] == 1:
                    max_area = max(dfs(i, j, vis), max_area)
                area = 0 
        
        return max_area 

             

        

            
        
        