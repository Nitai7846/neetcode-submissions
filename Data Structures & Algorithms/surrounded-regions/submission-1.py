class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m = len(board)
        n = len(board[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        def isValid(i,j,m,n):

            if i<0 or i>=m:
                return False
            
            if j<0 or j>=n:
                return False 
            
            return True 
        
        def dfs(i,j):

            if not isValid(i,j,m,n):
                return 
            
            if board[i][j] != 'O':
                return 
            
            board[i][j] = "#" 

            for di, dj in directions:

                ni, nj = i+di, j+dj

                if isValid(ni, nj, m, n) and board[ni][nj] == "O":
                    dfs(ni, nj)
        
        for j in range(0,n):
            dfs(0, j)
        
        for i in range(0, m):
            dfs(i, 0)
        
        for j in range(0, n):
            dfs(m-1, j)
        
        for i in range(0, m):
            dfs(i, n-1)
        
        for i in range(0, m):
            for j in range(0 ,n):
                if board[i][j] == "#":
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        
        
