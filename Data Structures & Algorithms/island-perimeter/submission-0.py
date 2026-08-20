class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        vis = [[False]*n for _ in range(m)]
        perimeter = 0 

        def isValid(i, j, m, n):

            if i<0 or i>=m:
                return False 
            if j<0 or j>=n:
                return False
            
            return True 
        
        def dfs(i, j, vis):

            if not isValid(i, j, m, n):
                return 1
            
            if vis[i][j]:
                return 0

            if grid[i][j] == 0:
                return 1
            
            vis[i][j] = True

            return (dfs(i-1, j, vis)+
            dfs(i+1, j, vis)+
            dfs(i, j-1, vis)+
            dfs(i, j+1, vis))

        
        for i in range(0, m):
            for j in range(0, n):
                if not vis[i][j] and grid[i][j] == 1:
                    perimeter = perimeter + dfs(i,j,vis)
        
        return perimeter 

                
                
            
            



        