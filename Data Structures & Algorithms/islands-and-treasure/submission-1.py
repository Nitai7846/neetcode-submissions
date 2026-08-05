class Solution:

    delRow = [-1,0,1,0]
    delCol = [0,1,0,-1]

    def isValid(self, i, j, m, n):
        if i<0 or i>=m:
            return False
        if j<0 or j>=n:
            return False 
        return True

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        m = len(grid)
        n = len(grid[0])

        q = deque()
        distance = 0
        for i in range(m):
            for j in range(n):

                if grid[i][j] == 0:
                    q.append((i,j,distance))

        while q:

            k = len(q)
            for _ in range(k):
                row, col, distance = q.popleft()
                for i in range(4):

                    nRow = row + self.delRow[i]
                    nCol = col + self.delCol[i]

                    if self.isValid(nRow, nCol, m, n) and grid[nRow][nCol] == 2147483647:
                        grid[nRow][nCol] = distance + 1
                        q.append((nRow, nCol, grid[nRow][nCol]))
                    


                    
                   

        
        

                



        