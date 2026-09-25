class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        delRow = [-1, 0, 1, 0]
        delCol = [0,-1,0,1]

        fresh = 0 
        m = len(grid)
        n = len(grid[0])

        minutes = 0 

        q = deque()

        def isValid(i,j,m,n):

            if i<0 or i>=m:
                return False
            if j<0 or j>=n:
                return False 
            return True
            

        for i in range(0,m):
            for j in range(0, n):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh+=1

        
        while q:

            k = len(q) 
            for _ in range(k):
                row, col = q.popleft()

                for i in range(0, 4):
                    nR, nC = row + delRow[i], col + delCol[i]

                    if isValid(nR, nC, m, n) and grid[nR][nC] == 1:
                        grid[nR][nC] = 2
                        fresh -= 1
                        q.append((nR, nC))
                
            if q:
                minutes+=1
        
        if fresh == 0:
            return minutes 
        else:
            return -1 



                    

               
                            

                    
                 

            

        
        