from collections import deque 
class Solution:

    delRow = [-1,0,1,0]
    delCol = [0,1,0,-1]

    def isValid(self, i, j, m, n):

        if i<0 or  i>=m:
            return False
        if j<0 or j>=n:
            return False
        
        return True 


    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        time = 0
        total = 0 
        count = 0 

        q = deque()

        for i in range(m):
            for j in range(n):

                if grid[i][j] != 0:
                    total+=1
                
                if grid[i][j] == 2:
                    q.append((i,j))
        
        while q:

            k = len(q)
            count += k 

            for _ in range(k):

                row, col = q.popleft()

                for i in range(4):

                    nRow = row + self.delRow[i]
                    nCol = col + self.delCol[i]

                    if  (self.isValid(nRow, nCol, m, n) and grid[nRow][nCol] == 1):
                        grid[nRow][nCol] = 2
                        q.append((nRow, nCol))
                    
            
            if q:
                time +=1 
        
        if total ==count:
            return time 
        
        return -1 







        