import sys 
sys.setrecursionlimit(100000)
class Solution:

    def isValid(self, row, col, newRow, newCol, m, n, matrix):

        if newRow < 0 or newRow >=m:
            return False
        
        if newCol < 0 or newCol >=n:
            return False
        
        if matrix[row][col] >= matrix[newRow][newCol] :
            return False
        
        return True
    
    def dfs(self, row, col, matrix, m, n, dp):

        if (row, col) in dp :
            return dp[(row, col)]

        lenght = 1
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        m = len(matrix)
        n = len(matrix[0])


        for combo in directions:

            newRow = row + combo[0]
            newCol = col + combo[1]

            if self.isValid(row, col, newRow, newCol, m, n, matrix):

                lenght = max(lenght, 1 + self.dfs(newRow, newCol, matrix, m,n, dp))

        dp[(row, col)] = lenght
        return dp[(row, col)]


    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        ans = 0 

        dp = {}

        for i in range(0, m):
            for j in range(0 , n):
                ans =  max(ans, self.dfs(i, j, matrix, m, n, dp))


        return ans 
        