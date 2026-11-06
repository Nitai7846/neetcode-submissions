class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])
        vis = [[False]*n for _ in range(m)]
        ans = False

        def isValid(i,j,m,n):
            if i<0 or i>=m:
                return False
            if j<0 or j>=n:
                return False
            return True 
        
    

        def dfs(i ,j, m, n, curr_len):

            if not isValid(i,j,m,n):
                return 
            
            if vis[i][j]:
                return 

            if board[i][j] != word[curr_len]:
                return False

            if curr_len == len(word) - 1:
                return True
            
            
            vis[i][j] = True
            found = (dfs(i+1, j, m, n, curr_len+1) or 
            dfs(i-1, j, m, n, curr_len+1) or 
            dfs(i, j+1, m, n, curr_len+1) or
            dfs(i, j-1, m, n, curr_len+1))
            vis[i][j] = False

            return found 
        
        start = 0
        curr_len = 0 
        
        for row in range(0, m):
            for col in range(0, n):
                if  board[row][col] == word[0]:
                    if dfs(row, col, m, n, 0):
                        return True 
        
        return False



            

        