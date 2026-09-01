class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        m = len(grid)
        n = len(grid[0])
        distance = 0

        def isValid(i,j,m,n):
            if i<0 or i>=m:
                return False 
            
            if j<0 or j>=n:
                return False 
            
            return True 
        
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        q = deque()

        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        while q:

            k = len(q)
            for _ in range(k):

                row, col = q.popleft()
                for di , dj in directions:
                    ni, nj = row+di, col+dj
                    if isValid(ni,nj,m,n) and grid[ni][nj] == 2147483647:
                        grid[ni][nj] = grid[row][col] + 1

                        q.append((ni, nj))
                    

                        

                







        