class Solution:

    def isValid(self, i, j, m, n):

        if i<0 or i>=m:
            return False 
        if j<0 or j>=n:
            return False 
        return True 
    
    def dfs(self, i, j, m, n):

        

        if not self.isValid(i, j, m, n):
            return 0 

        if i == m-1 and j == n-1:
            return 1 
        
        if self.memo[i][j]!=-1:
            return self.memo[i][j]
        
        self.memo[i][j] =  self.dfs(i+1, j , m, n) + self.dfs(i, j+1, m, n)
        
        return self.memo[i][j]


    def uniquePaths(self, m: int, n: int) -> int:
        self.memo = [[-1] * n for _ in range(m)]
        return self.dfs(0,0,m,n)




        