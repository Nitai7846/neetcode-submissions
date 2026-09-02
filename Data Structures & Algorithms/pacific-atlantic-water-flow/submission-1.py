class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m = len(heights)
        n = len(heights[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        vis_atlantic = [[False]*n for _ in range(m)]
        vis_pacific = [[False]*n for _ in range(m)]
        ans = []

        def isValid(i,j,m,n):

            if i<0 or i>=m:
                return False 
            if j<0 or j>=n:
                return False 
            return True 
        
        def dfs(r,c,vis):

            if not isValid(r,c,m,n):
                return  
            
            if vis[r][c]:
                return 

            vis[r][c] = True 

            for dr, dc in directions:

                nr, nc = r+dr, c+dc 
                if isValid(nr,nc,m,n) and not vis[nr][nc] and heights[nr][nc] >= heights[r][c]:
                    dfs(nr,nc,vis)

        for j in range(n):
            dfs(0,j,vis_pacific)
        
        for i in range(m):
            dfs(i, 0, vis_pacific)
                
        for j in range(n):
            dfs(m-1, j, vis_atlantic)
        
        for i in range(m):
            dfs(i, n-1, vis_atlantic)
        
        for i in range(0, m):
            for j in range(0 ,n):

                if vis_pacific[i][j] == True and vis_atlantic[i][j] == True:

                    ans.append([i,j])

        return ans

            



