class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        delRow = [-1,0,1,0]
        delCol = [0,-1,0,1]

        m = len(grid)
        n = len(grid[0])

        minute = 0
        fresh =0 

        def isValid(i,j,m,n):

            if i<0 or i>=m:
                return False 
            if j<0 or j>=n:
                return False 
            return True 
        
        q = collections.deque()

        for i in range(0,m):
            for j in range(0, n):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh+=1
        
        while q:

            k = len(q)
            for _ in range(k):
                row, col = q.popleft()
                for i in range(0,4):

                    nRow = row + delRow[i]
                    nCol = col + delCol[i]

                    if isValid(nRow, nCol, m, n) and grid[nRow][nCol] == 1:
                        grid[nRow][nCol] = 2
                        fresh -= 1
                        q.append((nRow, nCol))
            
            if q:
                minute+=1
        
        if fresh == 0:
            return minute
        else:
            return -1


        

        


        
        